import sys

from argparse import ArgumentParser
from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__author__ = "Adam Bobowski"


def parse_args():
    parser = ArgumentParser(description='Description')
    parser.add_argument('config_file', help="path to configuration file")
    return parser.parse_args()

# Global variables
args = parse_args()
config = ConfigParser()
config.read(args.config_file)
print(config.sections())


class DB:
    Base = declarative_base()
    engine = create_engine("{conn}://{user}:{pwd}@{url}/{db}".format(
        conn=config.get('Database', 'connection'),
        user=config.get('Database', 'login'),
        pwd=config.get('Database', 'password'),
        url=config.get('Database', 'url'),
        db=config.get('Database', 'database')
    ))
