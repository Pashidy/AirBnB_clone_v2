#!/usr/bin/python3
""" A script that starts a Flask web application to display specs """

from flask import Flask, render_template
from models import *
from models import storage

# Create a Flask app instance
app = Flask(__name__)

# Route for /hbnb
@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

# Route for the teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port='5000')
