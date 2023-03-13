# Hello World

```co2_trend
select * from "../../../target/co2_trend.parquet"
```

<LineChart
    data={co2_trend}
    x=date
    y=trend
    sort=sort_key
/>
