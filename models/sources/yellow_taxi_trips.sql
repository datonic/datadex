select
    VendorID as vendor_id,
    tpep_pickup_datetime as pickup_at,
    tpep_dropoff_datetime as dropoff_at,
    Passenger_count as passenger_count,
    Trip_distance as trip_distance,
    Payment_type as payment_type,
    Fare_amount as fare_amount,
    Tip_amount as tip_amount,
    Tolls_amount as tolls_amount,
    Total_amount as total_amount
from read_csv_auto('seeds/tripdata_20*.csv', header=1)