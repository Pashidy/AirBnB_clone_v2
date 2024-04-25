#!/usr/bin/python3
""" A script that starts a Flask web application to specific displays """

from flask import Flask, render_template
from models import *
from models import storage

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

# Route for the teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port='5000')
