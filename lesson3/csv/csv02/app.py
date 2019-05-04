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

population = []



def get_population():
    global header
    f = open('../census.csv', 'r')
    with f:
        reader = csv.reader(f)

        header = next(reader, None)  # skip the headers
        for row in reader:
            # if int(row[6]) > 3:
            population.append(row)
    return header, population


def save_population(size_of_household):
    f = open('names.csv', 'w')

    with f:
        writer = csv.writer(f)
        fnames = header

        writer.writerow(header)

        num = 0

        for row in population:
            if row[6] == size_of_household:
                writer.writerow(row)
                num += 1
    return num


app = Flask(__name__)


@app.route("/")
def index():
    header, rows = get_population()

    return render_template("index.html", rows=header)


@app.route("/other", methods=["POST"])
def other():
    size = request.form.get("num")
    num = save_population(size)
    return render_template("other.html", num=num)
