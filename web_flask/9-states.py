#!/usr/bin/python3
""" A script that starts a Flask web application Display specifications """

from flask import Flask, render_template
from models import *
from models import storage

# Create a Flask app instance
app = Flask(__name__)


# Route for states
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

# Route for the teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port='5000')
