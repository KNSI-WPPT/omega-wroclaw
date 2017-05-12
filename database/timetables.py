from sqlalchemy import Column, Integer, String, DateTime, Float

from database import DB


class Agency(DB.Base):
    __tablename__ = "agency"

    agency_id = Column(Integer, primary_key=True, nullable=False)
    agency_name = Column(String(32))
    agency_url = Column(String(32))  # Primary Key?
    agency_timezone = Column(String(32))
    agency_phone = Column(String(32))
    agency_lang = Column(String(4))


class Calendar(DB.Base):
    __tablename__ = "calendar"

    table_id = Column(Integer, primary_key=True, nullable=False)
    service_id = Column(Integer)
    monday = Column(Integer)
    tuesday = Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)
    sunday = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)


class CalendarDates(DB.Base):
    __tablename__ = "calendar_dates"

    table_id = Column(Integer, primary_key=True, nullable=False)
    service_id = Column(Integer)
    date = Column(Integer) #date 20170413
    exception_type = Column(Integer)


class ControlStops(DB.Base):
    __tablename__ = "control_stops"

    table_id = Column(Integer, primary_key=True, nullable=False)
    agency_id = Column (Integer)
    agency_name = Column(String(32))
    agency_url = Column(String(32))  # Primary Key?
    agency_timezone = Column(String(32))
    agency_phone = Column(String(32))
    agency_lang = Column(String(4))


class FeedInfo(DB.Base):
    __tablename__ = "feed_info"

    table_id = Column(Integer, primary_key=True, nullable=False)
    feed_publisher_name = Column(String(32))
    feed_publisher_url = Column(String(32))
    feed_lang = Column(String(32))
    feed_start_date = Column(String(32))
    feed_end_date = Column(String(32))


class Routes(DB.Base):
    __tablename__ = "routes"

    table_id = Column(Integer, primary_key=True, nullable=False)
    route_id = Column(String(10))
    agency_id = Column(Integer)
    route_short_name = Column(String(10))
    route_long_name = Column(String(10))
    route_desc = Column(String)
    route_type = Column(String(4))
    route_type2_id = Column (Integer)
    valid_from = Column (String) #data np "2017-03-06"
    valid_until = Column (String) #data też


class RoutesTypes(DB.Base):
    __tablename__ = "routes_types"

    table_id = Column(Integer, primary_key=True, nullable=False)
    route_type2_id = Column(Integer)
    route_type2_name = Column(String(32))


class StopTimes(DB.Base):
    __tablename__ = "stop_times"

    table_id = Column(Integer, primary_key=True, nullable=False)
    trip_id = Column(String(32)) #3_4861796
    arrival_time = Column(DateTime)  # 08:20:00
    departure_time = Column(DateTime) # 08:20:00
    stop_id = Column(Integer)
    stop_sequence = Column (Integer)
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)


class Trips(DB.Base):
    __tablename__ = "trips"

    table_id = Column(Integer, primary_key=True, nullable=False)
    route_id = Column(Integer)
    service_id = Column(Integer)
    trip_id = Column(String) #3_4861796
    trip_headsign = Column(String(32))
    direction_id = Column(Integer)
    brigade_id = Column(Integer)
    vehicle_id = Column(Integer)
    variant_id = Column(Integer)


class Variants(DB.Base):
    __tablename__ = "variants"

    table_id = Column(Integer, primary_key=True, nullable=False)
    variant_id = Column(Integer)
    is_main = Column(Integer)
    equiv_main_variant_id = Column(Integer)
    join_stop_id = Column(Integer)
    disjoin_stop_id = Column(Integer)


class VehicleTypes(DB.Base):
    __tablename__ = "vehicle_types"

    table_id = Column(Integer, primary_key=True, nullable=False)
    vehicle_type_id = Column(Integer)
    vehicle_type_name = Column(String(32))
    vehicle_type_description = Column(String(32))
    vehicle_type_symbol = Column(String(4)) #"N" lub ""
