#!/usr/bin/python3
""" A script that starts a Flask web applicationand displays 4 fxns """

from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'

# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route for C
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return 'C ' + text.replace('_', ' ')

# Route for python
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
