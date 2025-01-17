#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from flask import render_template

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
