{{ config(materialized="view") }}

with
    source as (select * from {{ source("ethereum", "blocks") }}),

    renamed as (
        select
            difficulty,
            hash,
            miner,
            nonce,
            number,
            size,
            timestamp,
            total_difficulty,
            base_fee_per_gas,
            gas_limit,
            gas_used,
            extra_data,
            logs_bloom,
            parent_hash,
            state_root,
            receipts_root,
            transactions_root,
            sha3_uncles,
            transaction_count,
            date,
            last_modified
        from source
    )

select *
from renamed
