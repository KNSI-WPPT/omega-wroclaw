from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////web/local.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from web import model, views