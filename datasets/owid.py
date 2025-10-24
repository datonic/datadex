import polars as pl

from datadex import dataset


@dataset
def owid_energy_data() -> pl.DataFrame:
    """
    Raw Energy data from Our World in Data.
    """
    energy_owid_url = (
        "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    )

    return pl.read_csv(
        energy_owid_url, try_parse_dates=True, infer_schema_length=None
    ).shrink_to_fit()


@dataset
def owid_co2_data() -> pl.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )

    return pl.read_csv(co2_owid_url)


@dataset
def owid_indicators(
    owid_energy_data: pl.DataFrame, owid_co2_data: pl.DataFrame
) -> pl.DataFrame:
    """
    Joined energy and CO2 data from Our World in Data.
    """

    df: pl.DataFrame = owid_energy_data.join(
        owid_co2_data, on=["iso_code", "year"], how="inner", suffix="_co2"
    )

    return df
