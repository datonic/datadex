with source as (
    select * from {{ source("carbon_intensity", "entry") }}
)

select * from source
