with yearly_co2_concentrations as (
    select
        Year as year,
        avg("CO2 concentrations (NOAA, 2018)") as average_CO2_concentrations
    from {{ ref('co2_concentrations') }}
    where Year > 2010 and Year < 2020
    group by 1
),

yearly_literate_population as (
    select
        Year as year,
        avg("Literacy rate (CIA Factbook (2016))") as average_literate_population
    from {{ ref('literate_population') }}
    where Year > 2010 and Year < 2020
    group by 1
)

select
    a.year,
    a.average_CO2_concentrations,
    b.average_literate_population
from yearly_co2_concentrations as a
left join yearly_literate_population as b
    on a.year = b.year