select country, iso_code, year, co2 from {{ source("public", "owid_co2_data") }}
