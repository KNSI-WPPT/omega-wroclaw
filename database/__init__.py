from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
import sys

__author__ = "Adam Bobowski"


def get_credentials(path):
    Config = ConfigParser()
    Config.read(path)
    section = 'Database'
    return 'mysql+pymysql://' + Config.get(section, 'login') + ':' + Config.get(section, 'password') + '@' + Config.get(section, 'url')

if (len(sys.argv) > 0):
    Base = declarative_base()
    engine = create_engine(get_credentials(sys.argv[1]))
    Session = sessionmaker(engine)
