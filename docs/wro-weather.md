# [`wro/weather`](todo)
## Sample
**Request**
```
GET TODO
```

**Response**
```
TODO
```

## Unified Data Format
### `weather.json`
```javascript
{
    "timestamp": number,
    "data_type": "weather",
    "data_group": "wro/weather",
    "data": [StationData]
}

StationData
{
    "location": string,
    "time": Date,
    "wind_velocity": number,
    "wind_direction": number,
    "temp_air": number,
    "temp_ground": number,
    "humidity": number,
    "fallout": string
}
```
- `location` - Location of weather station.
- `time` - When the data was registered by the station.
- `wind_velocity` - Velocity of wind in m/s.
- `wind_direction` - Direction of wind, in degrees.
- `temp_air` - Air temperature.
- `temp_ground` - Ground temperature.
- `humidity` - Air humidity.
- `fallout` - Type of fallout: `none`, `rain`
