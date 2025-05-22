import polars as pl


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

    return pl.read_csv(co2_owid_url)


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


def write_parquet(df: pl.DataFrame, path: str) -> None:
    """
    Write a DataFrame to a parquet file using Parquet version 2.0
    and sorted by iso_code and year for optimal query performance.
    """
    df = df.sort(["iso_code", "year"])
    df.write_parquet(
        path, 
        compression="snappy", 
        use_pyarrow=True, 
        pyarrow_options={"version": "2.0"},
        statistics=True
    )


def main() -> None:
    owid_energy_df = owid_energy_data()
    owid_co2_df = owid_co2_data()
    owid_indicators_df = owid_indicators(owid_energy_df, owid_co2_df)
    write_parquet(owid_indicators_df, "data/owid_indicators.parquet")


if __name__ == "__main__":
    main()
