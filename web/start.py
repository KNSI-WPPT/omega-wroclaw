import os
import sys

from threading import Lock
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, send_file, \
jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////web/local.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app,async_mode='eventlet')
thread = None
thread_lock = Lock()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


# TODO: connection between database file and SQLAlchemy
# db.create_all()

long1 = 16.97920383
long2 = 16.98920383
lat1 = 51.11058983
lat2 = 51.12058983


def background_thread():

    global long1, long2, lat1, lat2
    while True:
        socketio.sleep(5)

        data = {"bus_location_data": [

            {
                "id": "103",
                "longitude": round(long1,8),
                "latitude": round(lat1,8)
            },
            {
                "id": "100",
                "longitude": round(long2,8),
                "latitude": round(lat2,8)
            }]
        }
        socketio.emit('serial data',data)
        long1 = long1 + 0.001
        long2 = long2 + 0.001
        lat1 = lat1 + 0.001
        lat2 = lat2 + 0.001

@app.route('/')
def index():
    return render_template('maps.html',async_mode = socketio.async_mode)


@app.route('/maps')
def maps():
    return render_template('maps.html',async_mode = socketio.async_mode)


@app.route('/resources/<string:filename>')
def resources(filename):
    project_path = os.path.dirname(sys.modules['__main__'].__file__)
    return send_file(os.path.join(project_path + "/resources/" + filename))


@app.route('/resources/stops')
def get_stops():
    project_path = os.path.dirname(sys.modules['__main__'].__file__)
    f = open(os.path.join(project_path + "/resources/stops.txt"))
    lines = f.readlines()
    stops = []
    for i in range(len(lines)):
        line = lines[i].split(";")
        line_dict = {'lat': float(line[1].replace(',', '.')), 'lng': float(line[0].replace(',', '.')),
                     'id': int(line[2]), 'type': 1 if line[3].strip() == "3" else (0 if line[3].strip() == "0" else 2)}
        stops.append(line_dict)
    return jsonify({'stops': stops})


@socketio.on('connect')
def send_data():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':

    socketio.run(app, port=5000,host='localhost',debug=True)

