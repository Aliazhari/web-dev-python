from flask import Flask, render_template

# before you run flask run in th terminal, you need to set the envirement variable FLASK_APP
# export FLASK_APP=ex01.py (or whatever this file name is)

# if you get an error running flask that says adress is already in use,
# you need to kill the process first.
# first to find the process type in terminal:
# $ sudo lsof -i:5000
# kill XXXXX

# to avoid such error, make sure you terminate your flask application by CTRL + C

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello world!!!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!!"
    return render_template("index.html", headline=headline)