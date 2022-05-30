select
    year,
    avg(gdp) as avg_gdp,
    avg(electricity_generation) as avg_electricity_generation,
    avg(biofuel_electricity) as avg_biofuel_electricity,
    avg(coal_electricity) as avg_coal_electricity,
    avg(fossil_electricity) as avg_fossil_electricity,
    avg(gas_electricity) as avg_gas_electricity,
    avg(hydro_electricity) as avg_hydro_electricity,
    avg(nuclear_electricity) as avg_nuclear_electricity,
    avg(oil_electricity) as avg_oil_electricity,
    avg(renewables_electricity) as avg_renewables_electricity,
    avg(solar_electricity) as avg_solar_electricity,
    avg(wind_electricity) as avg_wind_electricity,
    avg(energy_per_gdp) as avg_energy_per_gdp,
    avg(energy_per_capita) as avg_energy_per_capita,
from {{ source('main', 'energy') }}
group by 1
order by 1 desc