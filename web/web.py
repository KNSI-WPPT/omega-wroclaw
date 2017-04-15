import os, sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/maps')
def maps():
    return render_template('maps.html')


@app.route('/stops')
def stops():
    project_path = os.path.dirname(sys.modules['__main__'].__file__)
    with open(os.path.join(project_path + "/resources/stops.txt")) as f:
        file_content = f.read()

    return file_content


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
