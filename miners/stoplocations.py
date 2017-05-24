import time
import threading

import requests

from database import DB
from database.stoplocations import StopLocation


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
        StopLocation.__table__.insert().prefix_with("OR REPLACE"),
        positions
    )


DB.Base.metadata.create_all(DB.engine)
connection = DB.engine.connect()


if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(60 * 60 * 24)
