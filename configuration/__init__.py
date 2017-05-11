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

print([(a, b) for a, b in config["SQLite"].items()])

class DB:
    Base = declarative_base()
    engine = create_engine(
        {
            "sqlite": "sqlite:///{path}",
            "mysql": "{conn}://{user}:{pwd}@{url}/{db}"
        }[config.sections()[0].tolower()].format(
            **config[config.sections()[0]]
        )
    )
