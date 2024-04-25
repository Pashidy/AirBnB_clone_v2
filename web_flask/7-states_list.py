#!/usr/bin/python3
""" A script that starts a Flask web application to specs """

from flask import Flask, render_template
from models import *
from models import storage


# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/states_list', strict_slashes=False)
def states_list():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

# Route for the teardown
@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
