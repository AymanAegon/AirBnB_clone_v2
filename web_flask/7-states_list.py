#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ function """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ function """
    return "HBNB"


@app.route("/c/<text>")
def ctext(text):
    """ function """
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>")
def pytext(text="is cool"):
    """ function """
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """ function """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ function """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """ function """
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = [s for s in storage.all(State).values()]
    print(states[0])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
