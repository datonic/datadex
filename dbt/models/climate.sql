with
    energy_data as (
        select year, sum(solar_electricity) as solar_electricity
        from {{ source("main", "owid_energy_data") }}
        where iso_code is not null and solar_electricity is not null and year >= 2014
        group by year
    ),
    co2_global_trend as (
        select year, avg(trend) as co2_trend
        from {{ source("main", "co2_global_trend") }}
        group by year
    )
select
    energy_data.year,
    energy_data.solar_electricity,
    co2_global_trend.co2_trend as co2_trend
from energy_data
left join co2_global_trend on energy_data.year = co2_global_trend.year
