with yearly_co2_concentrations as (
    select
        year,
        avg(CO2_concentrations) as average_CO2_concentrations
    from {{ ref('raw_co2_concentrations') }}
    where year > 2000 and year < 2010
    group by 1
),

yearly_literate_population as (
    select
        year,
        avg(literacy_rate) as average_literacy_rate
    from {{ ref('raw_literate_population') }}
    where year > 2000 and year < 2010
    group by 1
)

select
    co2.year,
    co2.average_CO2_concentrations,
    lp.average_literacy_rate
from yearly_co2_concentrations as co2
left join yearly_literate_population as lp
    on co2.year = lp.year