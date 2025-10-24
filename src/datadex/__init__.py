from __future__ import annotations

import argparse
import importlib
import inspect
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from types import FunctionType
from typing import Iterable, Iterator, TypeVar

import polars as pl

DATASETS_PACKAGE = "datasets"


@dataclass(frozen=True)
class DatasetDef:
    name: str
    module: str
    file_path: Path
    func: FunctionType

    @property
    def module_basename(self) -> str:
        return self.module.split(".")[-1]

    @property
    def storage_path(self) -> Path:
        dataset_root = self.file_path.parent.parent
        return dataset_root / "data" / self.file_path.stem / f"{self.name}.parquet"


_DATASETS: dict[str, DatasetDef] = {}
_DISCOVERED = False


F = TypeVar("F", bound=FunctionType)


def dataset(func: F) -> F:
    if not isinstance(func, FunctionType):
        raise TypeError("dataset decorator can only wrap function definitions")

    definition = DatasetDef(
        name=func.__name__,
        module=func.__module__,
        file_path=Path(inspect.getfile(func)).resolve(),
        func=func,
    )

    existing = _DATASETS.get(definition.name)
    if existing is not None and existing.func is not func:
        raise ValueError(
            f"Dataset '{definition.name}' already registered by {existing.module}."
        )

    _DATASETS[definition.name] = definition
    return func


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="dx",
        description="Datadex minimal dataset runner",
        epilog="Examples:\n  dx owid_co2_data\n  dx owid_indicators",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("dataset", nargs="?", help="Dataset to materialize")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild even if cached parquet already exists",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.dataset is None:
        parser.print_help()
        raise SystemExit(0)

    try:
        target = resolve_dataset(args.dataset)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    path, created = _materialize(target, force=args.force, visited=set())
    status = "Generated" if created else "Reused"
    print(f"{status} {target.name} -> {path}")


def _materialize(
    definition: DatasetDef, *, force: bool, visited: set[str]
) -> tuple[Path, bool]:
    if definition.name in visited:
        cycle = " -> ".join([*visited, definition.name])
        raise ValueError(f"Circular dependency detected: {cycle}")

    if definition.storage_path.exists() and not force:
        return definition.storage_path, False

    dependencies = []
    next_visited = visited | {definition.name}
    for dep_name in _dependency_names(definition):
        dependency = resolve_dataset(dep_name)
        dep_path, _ = _materialize(dependency, force=force, visited=next_visited)
        dependencies.append((dep_name, dep_path))

    inputs = {name: pl.read_parquet(path) for name, path in dependencies}

    result = definition.func(**inputs)
    if not isinstance(result, pl.DataFrame):
        raise TypeError(
            f"Dataset '{definition.name}' returned {type(result).__name__}, expected polars.DataFrame"
        )

    definition.storage_path.parent.mkdir(parents=True, exist_ok=True)
    result.write_parquet(definition.storage_path)
    return definition.storage_path, True


def resolve_dataset(target: str) -> DatasetDef:
    _ensure_discovered()

    module_hint, dataset_name = _split_target(target)

    direct = _DATASETS.get(target)
    if direct is not None and (
        module_hint is None or direct.module_basename == module_hint
    ):
        return direct

    matches = [
        definition
        for definition in _DATASETS.values()
        if definition.name == dataset_name
        and (module_hint is None or _matches_module(definition, module_hint))
    ]

    if not matches:
        available = ", ".join(sorted(_DATASETS)) or "<none>"
        raise ValueError(f"Dataset '{target}' not found. Available: {available}")

    if len(matches) > 1:
        options = ", ".join(
            f"{definition.module_basename}.{definition.name}"
            for definition in sorted(matches, key=lambda d: d.module_basename)
        )
        raise ValueError(
            f"Dataset '{dataset_name}' is ambiguous. Try one of: {options}"
        )

    return matches[0]


def _dependency_names(definition: DatasetDef) -> Iterator[str]:
    signature = inspect.signature(definition.func)
    for name, parameter in signature.parameters.items():
        if parameter.kind in (
            inspect.Parameter.POSITIONAL_ONLY,
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.KEYWORD_ONLY,
        ):
            yield name


def _split_target(target: str) -> tuple[str | None, str]:
    for separator in (".", "/"):
        if separator in target:
            module_hint, dataset_name = target.split(separator, 1)
            return module_hint, dataset_name
    return None, target


def _matches_module(definition: DatasetDef, module_hint: str) -> bool:
    return module_hint in {
        definition.module,
        definition.module_basename,
        f"{definition.module_basename}.py",
    }


def _ensure_discovered() -> None:
    global _DISCOVERED
    if _DISCOVERED:
        return

    datasets_directory = _datasets_directory()
    parent = datasets_directory.parent
    if str(parent) not in sys.path:
        sys.path.insert(0, str(parent))

    for path in sorted(datasets_directory.glob("*.py")):
        if path.name.startswith("_") or path.name == "__init__.py":
            continue
        module_name = f"{DATASETS_PACKAGE}.{path.stem}"
        importlib.import_module(module_name)

    _DISCOVERED = True


@lru_cache(maxsize=1)
def _datasets_directory() -> Path:
    candidates = []
    cwd = Path.cwd()
    candidates.extend(_candidate_directories(cwd))

    package_root = Path(__file__).resolve().parent.parent.parent
    candidates.append(package_root / DATASETS_PACKAGE)

    for directory in candidates:
        if directory.is_dir():
            return directory

    raise RuntimeError("Could not locate the datasets directory")


def _candidate_directories(base: Path) -> Iterator[Path]:
    for current in [base, *base.parents]:
        yield current / DATASETS_PACKAGE


__all__ = ["dataset", "main"]
