from sqlalchemy import Column, Integer, String,  Float

from database import DB


class StopLocation(DB.Base):
    __tablename__ = "stop_positions"

    lat = Column(Float)
    lon = Column(Float)
    stop_id = Column(Integer, primary_key=True)
    stop_type = Column(String(4))
