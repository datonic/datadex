select
    "Country Name"::string as country_name,
    "Country Code"::string as country_code,
    "Indicator Name"::string as indicator_name,
    "Indicator Code"::string as indicator_code,
    "Year"::integer as year,
    "Indicator Value"::double as indicator_value
from {{ source('main', 'world_bank_wdi') }}
