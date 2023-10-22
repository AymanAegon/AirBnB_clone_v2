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


@app.route("/states_list")
def states_list():
    """ function """
    l = storage.all(State)
    print(l)
    return render_template("7-states_list.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
