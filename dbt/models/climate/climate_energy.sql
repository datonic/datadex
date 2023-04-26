select
    *
from {{ source('web', 'energy') }}
