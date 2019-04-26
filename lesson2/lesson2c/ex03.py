from flask import Flask

# before you run flask run in th terminal, you need to set the envirement variable FLASK_APP
# export FLASK_APP=ex01.py (or whatever this file name is)

# if you get an error running flask that says adress is already in use,
# you need to kill the process first.
# first to find the process type in terminal:
# $ sudo lsof -i:5000
# kill XXXXX

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello {name}!"

