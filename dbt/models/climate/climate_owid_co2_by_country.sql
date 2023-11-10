select country, iso_code, year, co2 from {{ source("public", "raw_owid_co2_data") }}
