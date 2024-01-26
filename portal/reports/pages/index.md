---
title: Datadex Reports
---

_Beautiful reports with Evidence.dev_

<BarChart
  data={spain_energy_demand}
  y=year_average
  title="Spain Energy Demand"
/>


The average energy consumption in Spain in **<Value data={spain_energy_demand} column=year/>** is around **<Value data={spain_energy_demand} column=year_average/>** KW.


```sql spain_energy_demand
select
  year(cast(datetime as datetime)) as year,
  avg(value) as year_average
from spain_energy_demand
group by 1
order by 1 desc
```

<Alert status=info>
This is a demo!
</Alert>
