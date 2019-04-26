from flask import Flask, render_template, request, session
from flask_session import Session

# before you run flask run in th terminal, you need to set the envirement variable FLASK_APP
# export FLASK_APP=ex01.py (or whatever this file name is)

# if you get an error running flask that says adress is already in use,
# you need to kill the process first.
# first to find the process type in terminal:
# $ sudo lsof -i:5000
# kill XXXXX

# to avoid such error, make sure you terminate your flask application by CTRL + C

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("names") is None:
        session['names'] = []
    if request.method == "POST":
        name = request.form.get("name")
        session["names"].append(name)

    return render_template("index.html", names=session["names"])
