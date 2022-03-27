select
    VendorID as vendor_id,
    tpep_pickup_datetime as pickup_datetime,
    passenger_count,
    trip_distance
from read_csv_auto('seeds/tripdata_2020-*.csv', header=1)