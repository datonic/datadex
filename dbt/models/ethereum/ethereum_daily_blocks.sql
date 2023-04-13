select
    date,
    sum(transaction_count) as tx_count
from {{ ref('ethereum_blocks') }}
where
    date > '2023-01-01'
group by date
order by date
