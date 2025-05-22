import io
import zipfile

import httpx
import polars as pl


def world_development_indicators() -> pl.DataFrame:
    """
    World Development Indicators (WDI) is the World Bank's premier compilation of cross-country comparable data on development.

    Bulk data download is available at https://datatopics.worldbank.org/world-development-indicators/
    """

    url = "https://databankfiles.worldbank.org/public/ddpext_download/WDI_CSV.zip"

    response = httpx.get(url)

    zipfile.ZipFile(io.BytesIO(response.content)).extractall(path="/tmp/")

    # Load the WDICSV.csv file as a DataFrame
    df = pl.read_csv("/tmp/WDICSV.csv")

    # Reshape the dataframe
    df = df.unpivot(
        index=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_name="Indicator Value",
        variable_name="Year",
    )

    df = df.with_columns(pl.col("Year").cast(pl.Int32))

    df = df.rename({
        "Country Name": "country_name",
        "Country Code": "country_code",
        "Indicator Name": "indicator_name",
        "Indicator Code": "indicator_code",
        "Year": "year",
        "Indicator Value": "indicator_value",
    })

    df = df.drop_nulls(subset=["indicator_value"])

    return df


def main() -> None:
    df = world_development_indicators()
    # Sort by country_code, year, and indicator_code for optimal query performance
    df = df.sort(["country_code", "year", "indicator_code"])
    df.write_parquet(
        "data/world_development_indicators.parquet",
        compression="snappy",
        use_pyarrow=True,
        pyarrow_options={"version": "2.0"},
        statistics=True
    )


if __name__ == "__main__":
    main()
