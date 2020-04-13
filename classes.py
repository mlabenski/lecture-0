from flask import Flask, render_template

import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    easter = now.month == 4 and now.day == 12
    return render_template("index.html", easter=easter)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
