import polars as pl

from datadex import materialize


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


def owid_co2_data() -> pl.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )

    return pl.read_csv(
        co2_owid_url, try_parse_dates=True, infer_schema_length=None
    ).shrink_to_fit()


def owid_indicators() -> pl.DataFrame:
    """
    Joined energy and CO2 data from Our World in Data.
    """

    df: pl.DataFrame = owid_energy_data().join(
        owid_co2_data(), on=["iso_code", "year"], how="inner", suffix="_co2"
    )

    return df.sort(["iso_code", "year"])


def main() -> None:
    materialize(owid_indicators)


if __name__ == "__main__":
    main()
