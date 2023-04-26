from dagster import asset
import urllib.request


@asset
def bsky() -> None:
    urllib.request.urlretrieve(
        "https://huggingface.co/datasets/andrewconner/bluesky_profiles/resolve/main/bsky.db",
        "data/bsky.db",
    )
