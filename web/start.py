import os
import sys

from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, send_file, \
    jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////web/local.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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
db.create_all()


@app.route('/')
def index():
    return render_template('maps.html')


@app.route('/maps')
def maps():
    return render_template('maps.html')


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


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
