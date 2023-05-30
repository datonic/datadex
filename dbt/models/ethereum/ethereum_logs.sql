{{ config(materialized="view") }}

with
    source as (select * from {{ source("ethereum", "logs") }}),

    renamed as (
        select
            date,
            log_index,
            transaction_hash,
            transaction_index,
            address,
            data,
            topics,
            block_timestamp,
            block_number,
            block_hash
        from source
    )

select *
from renamed
