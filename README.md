# Omega - Wrocław

## Start Miners
Starting miner requires path to configuration file that holds details of database where the data will be stored. At this momemnt **SQLite** as local database, and **MySQL** as remote database, are supported.

### `SQLite.ini`
```ini
[SQLite]
path = local_db.db
```

### `MySQL.ini`
```ini
[MySQL]
connection = mysql+pymysql
url = <database url>
database = <database>
login = <login>
password = <password>
```


## Util scripts

### `mysql backup`
```bash
mysqldump.exe -h <instance address> -u <login> -p <remote db> --single-transaction > dump.sql
```

### `mysql load to local`
```
mysql.exe -u <local user name> -p <local db> < dump.sql
```
