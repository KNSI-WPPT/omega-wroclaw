import time
import threading

import requests
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

from database import DB
from database.stoplocations import StopLocation


@compiles(Insert)
def append_string(insert, compiler, **kw):
    s = compiler.visit_insert(insert, **kw)
    if 'append_string' in insert.kwargs:
        return s + " " + insert.kwargs['append_string']
    return s


def fetch_data():
    r = requests.get('http://geoportal.wroclaw.pl/www/pliki/KomunikacjaZbiorowa/SlupkiWspolrzedne.txt')

    positions = []
    for line in r.text.splitlines():
        line = line.strip()
        if not line:
            continue

        lon, lat, stop_id, stop_type = line.split(';')

        positions.append({
            "lon": float(lon.replace(",", ".")),
            "lat": float(lat.replace(",", ".")),
            "stop_id": int(stop_id),
            "stop_type": stop_type
        })

    connection.execute(
        StopLocation.__table__.insert(
            append_string='ON DUPLICATE KEY UPDATE lon=VALUES(lon), lat=VALUES(lat), stop_type=VALUES(stop_type)'),
        positions
    )


DB.Base.metadata.create_all(DB.engine)
connection = DB.engine.connect()

if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(60 * 60 * 24)
