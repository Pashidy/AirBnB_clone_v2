#!/usr/bin/python3
""" A script that starts a Flask web application that has 3 display fxns """

from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route for C
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
