select
    vendor_id,
    min(pickup_datetime) as first_trip,
    max(pickup_datetime) as last_trip,
    avg(passenger_count) as avg_passenger_count,
    avg(trip_distance) as avg_trip_distance
from {{ ref('raw_taxi_tripdata') }}
group by 1