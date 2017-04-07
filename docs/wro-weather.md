# [`wro/weather`](todo)
## Sample
**Request**
```
GET http://www.wroclaw.pl/open-data/opendata/its/pogoda/pogoda.csv
```

**Response**
```
Czas_Rejestracji;Wiatr_V;Wiatr_Kierunek;Wilgotnosc;T_Powietrza;T_Grunt;Opad_Typ;Lokalizacja_Opis
2017-04-05 00:00:00.000;1.3;278.90;94.80;10.80;11.50;69;UL. LOTNICZA / UL. KOSMONAUTÓW
2017-04-05 00:00:00.000;1.09;273.00;94.56;10.20;12.49;69;MOST ROMANA DMOWSKIEGO
2017-04-05 00:00:00.000;2.5;222.20;87.50;9.90;11.10;69;AL. JANA III SOBIESKIEGO
2017-04-05 00:00:00.000;2.2;302.10;90.60;10.10;14.00;69;UL. OPOLSKA / UL. KATOWICKA
2017-04-05 00:00:00.000;0;235.00;96.42;9.69;11.25;69;ESTAKADA GADOWIANKA
2017-04-05 00:00:00.000;2.7;306.40;93.60;11.40;11.60;69;MOST MILENIJNY
...
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
- `fallout` - Type of fallout: `"none" < "passing" < "constant" < "heavy"`.
