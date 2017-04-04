# UDF - Unified Data Format
Crawling from different locations might cause some formatting issues. Introducing UDF is meant to resolve compatibility issues and provide general interface for data management and operations.
UDF is just a Json format with some fixed properties.

## `udf.json`
```javascript
{
  "timestamp": number,
  "data_type": string,
  "data_group": string,
  "data": [DataObjects]
}
```

- `timestamp` - Timestamp of when the data was gathered. Seconds of `time.time()`.
- `data_type` - Name of gathered data. Should match filename for clarity.
- `data_group` - Gather group of data files under the same group name. Should match directory structure.
- `data` - List of crawled data objects.

## Dates & Timestamps
It's possible to encounter different date formats in crawled raw files.
In udf file date must be in one of standard date formats as `ISO-8601` or `Unix time`.
It's recommended that `Unix time` is used only for `timestamp` property because this field does not need to be always human readable. `ISO-8601` format for all other dates, specially for calendars. Timezone should be either explicitly specified or assumed UTC by default.
`ISO-8601` date should have `YYY-MM-DDThh:mm:ss±hh:mm` format.

**Example:**
```javascript
ExampleObject
{
  ...
  "timestamp": 1491312861,
  "date": "2004-02-12T15:19:21+00:00",
  ...
}
```

## GPS Coordinates
GPS coordinates should be represented by list of two values: latitude and longitude and named `coordinates` or similar.

**Example**
```javascript
ExampleObject
{
  ...
  "coordinates": [40.741895, -73.989308],
  ...
}
```
