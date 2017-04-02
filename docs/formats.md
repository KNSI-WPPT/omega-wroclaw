# Data Formats
Data gathered from different endpoints has to be somehow unified for further use.

## UDFormat - Unified Data Format
Data format unified after crawling data from source.
Unification should clarify access interface to data.
Json format with fixed properties.

```javascript
{
    timestamp: number,
    data_type: string,
    data_group: string,
    data: [object]
}
```

## [`MPK/positions`](http://pasazer.mpk.wroc.pl/jak-jezdzimy/mapa-pozycji-pojazdow)
### Example Request
**Input:**
```
POST http://pasazer.mpk.wroc.pl/position.php`
Form Data:
busList[bus][]:d
busList[bus][]:k
```

**Output:**
```javascript
[{"name":"d","type":"bus","y":16.969368,"x":51.06806,"k":9428173},{"name":"k","type":"bus","y":17.03524,"x":51.099575,"k":9429405},{"name":"k","type":"bus","y":17.026419,"x":51.141346,"k":9429438},{"name":"d","type":"bus","y":17.133308,"x":51.159653,"k":9428205},{"name":"k","type":"bus","y":17.04286,"x":51.148205,"k":9429422},{"name":"k","type":"bus","y":17.046026,"x":51.077015,"k":9429388},{"name":"d","type":"bus","y":16.984161,"x":51.063988,"k":9428252},{"name":"d","type":"bus","y":17.11131,"x":51.14576,"k":9428281},{"name":"d","type":"bus","y":17.01257,"x":51.08704,"k":9428266},{"name":"d","type":"bus","y":17.028986,"x":51.100895,"k":9428227},{"name":"d","type":"bus","y":17.077965,"x":51.12166,"k":9427681},{"name":"d","type":"bus","y":16.998318,"x":51.078175,"k":9428239},{"name":"d","type":"bus","y":17.060501,"x":51.111664,"k":9428189}]
```

### UDFormat
#### `position.json`
```javascript
{
    timestamp: number,
    data_type: "positions",
    data_group: "mpk/positions",
    data: [Vehicle]
}

Vehicle
{
    name: string,  # Line
    type: string,  # "bus" or "tram"
    y: number      # GPS position
    x: number      # GPS position
    k: number      # Unique course number
}
```

## [`MPK/timetables`](http://www.wroclaw.pl/open-data/index.php/zbiory-danych/17-transport/106-rozklad-jazdy-transportu-publicznego)
### Example Request
**Input:**
```
GET http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip
```

**Output:**
```
Zip archive
```

### UDFormat
#### `agency.json`
```javascript
{
    timestamp: number,
    data_type: "agency",
    data_group: "mpk/timetables",
    data: [Agency]
}

Agency
{
    agency_id: number
    agency_name: string
    agency_url: string
    agency_timezone: string
    agency_phone: string
    agency_lang: string
}
```

#### `calendar_dates.json`
```javascript
{
    timestamp: number,
    data_type: "calendar_dates",
    data_group: "mpk/timetables",
    data: [CalendarDate]
}

CalendarDate
{
    service_id: number,
    date: number,
    exception_type: number
}
```

#### `calendar.json`
```javascript
{
    timestamp: number,
    data_type: "calendar",
    data_group: "mpk/timetables",
    data: [Calendar]
}

Calendar
{
    service_id: number,
    monday: number,
    tuesday: number,
    wednesday: number,
    thursday: number,
    friday: number,
    saturday: number,
    sunday: number,
    start_date: number,
    end_date: number
}
```

#### `control_stops.json`
```javascript
{
    timestamp: number,
    data_type: "control_stops",
    data_group: "mpk/timetables",
    data: [ControlStops]
}

CalendarStops
{
    variant_id: number,
    stop_id: number
}
```

#### `feed_info.json`
```javascript
{
    timestamp: number,
    data_type: "feed_info",
    data_group: "mpk/timetables",
    data: [FeedInfo]
}

FeedInfo
{
    feed_publisher_name: string,
    feed_publisher_url: string,
    feed_lang: string,
    feed_start_date: string,
    feed_end_date: string
}
```

#### `route_types.json`
```javascript
{
    timestamp: number,
    data_type: "route_types",
    data_group: "mpk/timetables",
    data: [RouteType]
}

RouteType
{
    route_type2_id: number,
    route_type2_name: string
}
```

#### `routes.json`
```javascript
{
    timestamp: number,
    data_type: "routes",
    data_group: "mpk/timetables",
    data: [Route]
}

Route
{
    route_id: number,
    agency_id: number,
    route_short_name: string,
    route_long_name: string,
    route_desc: string,
    route_type: number,
    route_type2_id: number,
    valid_from: string,
    valid_until: string
}
```

#### `stop_times.json`
```javascript
{
    timestamp: number,
    data_type: "stop_times",
    data_group: "mpk/timetables",
    data: [StopTime]
}

StopTime
{
    trip_id: string,
    arrival_time: string,
    departure_time: string,
    stop_id: number,
    stop_sequence: number,
    pickup_type: number,
    drop_off_type: number
}
```

#### `stops.json`
```javascript
{
    timestamp: number,
    data_type: "stops",
    data_group: "mpk/timetables",
    data: [Stop]
}

Stop
{
    stop_id: number,
    stop_code: number,
    stop_name: string,
    stop_lat: number,
    stop_lon: number
}
```

#### `trips.json`
```javascript
{
    timestamp: number,
    data_type: "trips",
    data_group: "mpk/timetables",
    data: [Trip]
}

Trip
{
    route_id: number,
    service_id: number,
    trip_id: string,
    trip_headsign: string,
    direction_id: number,
    brigade_id: number,
    vehicle_id: number,
    variant_id: number
}
```

#### `variants.json`
```javascript
{
    timestamp: number,
    data_type: "variants",
    data_group: "mpk/timetables",
    data: [Variant]
}

Variant
{
    variant_id: number,
    is_main: number,
    equiv_main_variant_id: number,
    join_stop_id: number,
    disjoin_stop_id: number
}
```

#### `vehicle_types.json`
```javascript
{
    timestamp: number,
    data_type: "vehicle_types",
    data_group: "mpk/timetables",
    data: [VehicleType]
}

VehicleType
{
    vehicle_type_id: number,
    vehicle_type_name: string,
    vehicle_type_description: string,
    vehicle_type_symbol: string
}
```