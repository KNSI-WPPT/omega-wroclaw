import requests
import time
import datetime

from database import DB



DB.Base.metadata.create_all(DB.engine)
connection = DB.engine.connect()

