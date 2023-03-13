select 
  make_date(year, month, day) as date, 
  year < 2020 as d,
  * 
from co2_trend_gl
order by 1 asc