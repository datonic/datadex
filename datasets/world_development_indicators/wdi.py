import io
import warnings
import zipfile

import httpx
import polars as pl

from datadex import materialize


def fetch_bytes(
    url: str,
    *,
    timeout: float | httpx.Timeout = 120.0,
    follow_redirects: bool = True,
) -> bytes:
    """Download the content at ``url`` and return the raw bytes.

    The request is attempted with standard TLS verification. If that fails due to
    certificate validation errors (common behind corporate proxies), a single
    retry is performed with verification disabled while emitting a warning.
    """

    headers = {"User-Agent": "datadex/0.1"}

    try:
        response = httpx.get(
            url,
            follow_redirects=follow_redirects,
            timeout=timeout,
            headers=headers,
        )
    except httpx.HTTPError as exc:
        if "CERTIFICATE_VERIFY_FAILED" not in repr(exc):
            raise

        warnings.warn(
            f"Falling back to insecure TLS download for {url}",
            RuntimeWarning,
            stacklevel=2,
        )
    else:
        response.raise_for_status()
        return response.content

    response = httpx.get(
        url,
        follow_redirects=follow_redirects,
        timeout=timeout,
        headers=headers,
        verify=False,
    )
    response.raise_for_status()
    return response.content


def world_development_indicators() -> pl.DataFrame:
    """
    World Development Indicators (WDI) is the World Bank's premier compilation of cross-country comparable data on development.

    Bulk data download is available at https://datatopics.worldbank.org/world-development-indicators/
    """

    url = "https://databank.worldbank.org/data/download/WDI_CSV.zip"

    archive_bytes = fetch_bytes(url, timeout=300.0)

    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        with archive.open("WDICSV.csv") as csv_file:
            df = pl.read_csv(csv_file)

    # Reshape the dataframe
    df = df.unpivot(
        index=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_name="Indicator Value",
        variable_name="Year",
    )

    df = df.with_columns(pl.col("Year").cast(pl.Int32))

    df = df.rename(
        {
            "Country Name": "country_name",
            "Country Code": "country_code",
            "Indicator Name": "indicator_name",
            "Indicator Code": "indicator_code",
            "Year": "year",
            "Indicator Value": "indicator_value",
        }
    )

    df = df.drop_nulls(subset=["indicator_value"])

    return df.sort(["country_code", "year", "indicator_code"])


def main() -> None:
    materialize(world_development_indicators)


if __name__ == "__main__":
    main()
