with source as (
    select * from {{ source('github', 'yellow_taxi_trips') }}
),

renamed as (
    select
        vendorid as vendor_id,
        passenger_count,
        trip_distance,
        pickup_longitude,
        pickup_latitude,
        ratecodeid as ratecode_id,
        dropoff_longitude,
        dropoff_latitude,
        payment_type,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        pickup_time,
        pickup_date,
        dropoff_time,
        dropoff_date
    from source
)

select * from renamed
