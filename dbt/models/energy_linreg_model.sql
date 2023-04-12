select
    *
from {{
  dbt_linreg.ols(
    table=ref('energy_yearly_averages'),
    endog='avg_gdp',
    exog=['avg_electricity_generation', 'avg_solar_electricity', 'avg_wind_electricity'],
    format='long',
    format_options={'round': 5}
  )
}}
