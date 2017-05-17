from argparse import ArgumentParser
from configparser import ConfigParser

from sqlalchemy import create_engine
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


class DB:
    Base = declarative_base()
    engine = create_engine(
        {
            "sqlite": "sqlite:///{path}",
            "mysql": "{connection}://{login}:{password}@{url}/{database}"
        }[config.sections()[0].lower()].format(
            **config[config.sections()[0]]
        )
    )
