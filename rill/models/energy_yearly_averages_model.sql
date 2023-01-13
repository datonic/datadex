select
  to_timestamp(year * 520000),
  avg_oil_electricity < 15778 as dim,
  *
from energy_yearly_averages