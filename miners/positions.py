import requests
import time
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

from configuration import DB


class Position(DB.Base):
    __tablename__ = "vehicle_positions"

    id = Column(Integer, primary_key=True, nullable=False)
    datetime = Column(DateTime)
    name = Column(String(32))  # Primary Key?
    type = Column(String(32))
    x = Column(Float)
    y = Column(Float)
    k = Column(Float)


DB.Base.metadata.create_all(DB.engine)

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
    print("Fetching data...\r")
    r = requests.post(
        'http://mpk.wroc.pl/position.php',
        data={"busList[bus][]": buses, "busList[tram][]": trams},
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    print("Adding...\r")
    now = datetime.datetime.now()
    t0 = time.time()
    positions = []
    for j in r.json():
        j['datetime'] = now
        positions.append(j)
    DB.engine.execute(
        Position.__table__.insert(),
        positions
    )
    print("Added in " + str(time.time() - t0) + "secs")


# TODO Nice daemon process with error handling
while True:
    print("Crawling...\r")
    fetch_data(buses, trams)
    print("Sleeping...\r")
    time.sleep(10)
