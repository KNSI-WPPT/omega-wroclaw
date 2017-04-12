import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
