from flask import Flask, render_template, request
import csv

# before you run flask run in th terminal, you need to set the envirement variable FLASK_APP
# export FLASK_APP=ex01.py (or whatever this file name is)

# if you get an error running flask that says adress is already in use,
# you need to kill the process first.
# first to find the process type in terminal:
# $ sudo lsof -i:5000
# kill XXXXX

# to avoid such error, make sure you terminate your flask application by CTRL + C


def get_population():
    population = []
    f = open('../census.csv', 'r')
    with f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for row in reader:
            if int(row[6]) > 3:
                population.append(row)
    return population

app = Flask(__name__)


@app.route("/")
def index():
    rows = get_population()
    return render_template("index.html", rows=rows)

