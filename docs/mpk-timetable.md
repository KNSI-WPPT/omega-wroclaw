# [`mpk/timetables`](http://www.wroclaw.pl/open-data/index.php/zbiory-danych/17-transport/106-rozklad-jazdy-transportu-publicznego)
## Sample
**Request**
```
GET http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip
```

**Response**
```
Zip archive
```

## Unified Data Format
### `agency.json`
```javascript
{
    "timestamp": number,
    "data_type": "agency",
    "data_group": "mpk/timetables",
    "data": [Agency]
}

Agency
{
    "agency_id": number
    "name": string
    "url": string
    "timezone": string
    "phone": string
    "language": string
}
```
- `agency_id` - Unique id of agency.
- `name` - `agency_name` in raw data.
- `url` - `agency_url` in raw data.
- `timezone` - `agency_timezone` in raw data.
- `phone` - `agency_phone` in raw data.
- `language` - `agency_lang` in raw data.


### `calendar_dates.json`
```javascript
{
    "timestamp": number,
    "data_type": "calendar_dates",
    "data_group": "mpk/timetables",
    "data": [CalendarDate]
}

CalendarDate
{
    "service_id": number,
    "date": Date,
    "exception_type": number
}
```
`// TODO`

### `calendar.json`
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
`// TODO`

### `control_stops.json`
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

### `route_types.json`
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

### `routes.json`
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

### `stop_times.json`
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

### `stops.json`
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

### `trips.json`
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

### `variants.json`
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

### `vehicle_types.json`
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
