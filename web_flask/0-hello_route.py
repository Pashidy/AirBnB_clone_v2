#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
