import os, sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, send_file, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


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
        line_dict = {'lat' : float(line[0].replace(',', '.')), 'lgn': float(line[1].replace(',', '.')),
                     'id': int(line[2]), 'type': 1 if line[3] == '3' else (0 if line[3] == '0' else 2)}
        stops.append(line_dict)
    return jsonify({'stops': stops})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
