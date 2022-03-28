select
    vendor_id,
    min(pickup_at) as first_trip,
    max(pickup_at) as last_trip,
    avg(passenger_count) as avg_passenger_count,
    avg(trip_distance) as avg_trip_distance
from {{ ref('yellow_taxi_trips') }}
where
    vendor_id is not null
group by 1