import time
import datetime
import pytz
import requests
import threading

from database import DB
from database.positions import Position


# TODO Fetch bus & tram lines from DB
buses = [
    '100', '103', '105', '107', '109', '110', '113', '114', '115', '116', '118', '119', '120', '122', '125', '126',
    '127', '128', '129', '130', '131', '132', '133', '134', '136', '140', '141', '142', '144', '145', '146', '147',
    '149', '240', '241', '243', '245', '246', '247', '249', '250', '251', '253', '255', '257', '259', '406', '409',
    'a', 'c', 'd', 'k', 'n'
]
trams = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '14', '15', '17', '20', '23', '24', '31', '32', '33',
    '0p', '0l'
]


def fetch_data(buses, trams):
    now = datetime.datetime.now(pytz.timezone('Europe/Warsaw'))

    r = requests.post(
        'http://mpk.wroc.pl/position.php',
        data={"busList[bus][]": buses, "busList[tram][]": trams},
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    positions = r.json()
    for p in positions:
        p['datetime'] = now

    connection.execute(
        Position.__table__.insert(),
        positions
    )


DB.Base.metadata.create_all(DB.engine)
connection = DB.engine.connect()

if __name__ == "__main__":
    while True:
        threading.Timer(10, fetch_data, args=[buses, trams]).start()
        time.sleep(10)

