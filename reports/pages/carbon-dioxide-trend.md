# Trends in Atmospheric Carbon Dioxide

```co2_global_trend
select * from "../../../data/co2_global_trend.parquet"
```

<LineChart
    data={co2_global_trend}
    x=date
    y=trend
    yAxisTitle="Averaged CO2"
    sort=date
    yMin={380}
/>

Averaged CO2 from four GML Atmospheric Baseline observatories
