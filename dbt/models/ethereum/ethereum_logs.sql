{% set r2_setup %}
SET s3_region="auto";
SET s3_endpoint='ed5d915e0259fcddb2ab1ce5592040c3.r2.cloudflarestorage.com';
SET s3_access_key_id='43c31ff797ec2387177cabab6d18f15a';
SET s3_secret_access_key='afb354f05026f2512557922974e9dd2fdb21e5c2f5cbf929b35f0645fb284cf7';
SET s3_url_style='path';
{% endset %}

{% set results = run_query(r2_setup) %}

select *
from
    parquet_scan(
        's3://indexed-xyz/ethereum/decoded/logs/v1.2.0/partition_key=9d/dt=2023/*.parquet',
        hive_partitioning = 1
    )
