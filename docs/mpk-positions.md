# [`mpk/positions`](http://pasazer.mpk.wroc.pl/jak-jezdzimy/mapa-pozycji-pojazdow)
## Sample
**Request**
```
POST http://pasazer.mpk.wroc.pl/position.php`
Form Data:
busList[bus][]:d
busList[bus][]:k
```

**Response**
```javascript
[{"name":"d","type":"bus","y":16.969368,"x":51.06806,"k":9428173},{"name":"k","type":"bus","y":17.03524,"x":51.099575,"k":9429405},{"name":"k","type":"bus","y":17.026419,"x":51.141346,"k":9429438},{"name":"d","type":"bus","y":17.133308,"x":51.159653,"k":9428205},{"name":"k","type":"bus","y":17.04286,"x":51.148205,"k":9429422},{"name":"k","type":"bus","y":17.046026,"x":51.077015,"k":9429388},{"name":"d","type":"bus","y":16.984161,"x":51.063988,"k":9428252},{"name":"d","type":"bus","y":17.11131,"x":51.14576,"k":9428281},{"name":"d","type":"bus","y":17.01257,"x":51.08704,"k":9428266},{"name":"d","type":"bus","y":17.028986,"x":51.100895,"k":9428227},{"name":"d","type":"bus","y":17.077965,"x":51.12166,"k":9427681},{"name":"d","type":"bus","y":16.998318,"x":51.078175,"k":9428239},{"name":"d","type":"bus","y":17.060501,"x":51.111664,"k":9428189}]
```

## Unified Data Format
### `positions.json`
```javascript
{
  "timestamp": number,
  "data_type": "positions",
  "data_group": "mpk/positions",
  "data": [Vehicle]
}

Vehicle
{
    "name": string,
    "type": string,
    "coordinates": Coordinates,
    "course": number
}
```
- `name` - Name of vehicle ("d", "0l", etc.)
- `type` - `"bus"` or `"tram"`.
- `coordinates` - GPS coordinates, udf compatible. `x` and `y` in raw data.
- `course` - Current unique id of vehicle course. `k` in raw data.
