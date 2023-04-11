with source as (
      select * from {{ source('github', 'co2_global_trend') }}
),

renamed as (
    select
        make_date(year, month, day) as date,
        trend
    from source
    order by 1 asc
)

select * from renamed
