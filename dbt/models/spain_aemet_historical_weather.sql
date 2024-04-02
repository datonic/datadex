select
    cast(w.fecha as date) as fecha,
    w.indicativo,
    w.nombre,
    w.provincia,
    s.latitud,
    s.longitud,
    cast(w.altitud as int) as altitud,
    cast(w.tmed as float) as tmed,
    cast(w.prec as float) as prec,
    cast(w.tmin as float) as tmin,
    w.horatmin,
    cast(w.tmax as float) as tmax,
    w.horatmax,
    cast(w.dir as int) as dir,
    cast(w.velmedia as float) as velmedia,
    cast(w.racha as float) as racha,
    w.horaracha,
    cast(w.presMax as float) as presMax,
    w.horaPresMax,
    cast(w.presMin as float) as presMin,
    w.horaPresMin,
    cast(w.hrMedia as int) as hrMedia,
    cast(w.hrMax as int) as hrMax,
    w.horaHrMax,
    cast(w.hrMin as int) as hrMin,
    w.horaHrMin,
    cast(w.sol as float) as sol
from {{ source('main', 'spain_aemet_weather_data') }} as w
left join {{ source('main', 'spain_aemet_stations_data') }} as s
    on w.indicativo = s.indicativo
order by w.fecha, w.indicativo
