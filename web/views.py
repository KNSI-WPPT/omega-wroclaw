import os
import sys
from flask import render_template, send_file, jsonify, redirect
from config import app


@app.route('/')
def index():
    return redirect("/maps", code=302)


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
                     'id': int(line[2]),
                     'type': 1 if line[3].strip() == "3" else (0 if line[3].strip() == "0" else 2)}
        stops.append(line_dict)
    return jsonify({'stops': stops})
