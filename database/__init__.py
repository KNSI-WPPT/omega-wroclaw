from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__author__ = "Adam Bobowski"

Base = declarative_base()
# TODO SQL database on AWS
# TODO Credentials in config file
engine = create_engine('sqlite:///sqlalchemy_example.db')
Session = sessionmaker(engine)