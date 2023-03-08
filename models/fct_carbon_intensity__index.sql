with 

    entries as (
        select * from {{ source("carbon_intensity", "entry") }}
    ),

    regions as (
        select * from {{ source("carbon_intensity", "region") }}
    ),

    final as (
        select
            regions.shortname as region_name,
            cast(replace(entries.from, 'T', ' ')[:-1]||':00' as timestamp) as start_ts,
            cast(replace(entries.to, 'T', ' ')[:-1]||':00' as timestamp) as end_ts,
            entries.forecast as carbon_intensity,
            entries.index as carbon_index,
            cast(replace(entries.to, 'T', ' ')[:-1]||':00' as timestamp)
            - cast(replace(entries.from, 'T', ' ')[:-1]||':00' as timestamp) as period
        from
            entries
        left join
            regions on (entries.region_id = regions.id)
    )

select * from final
