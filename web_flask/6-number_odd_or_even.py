#!/usr/bin/python3
""" A  Python script using Flask to create a web application with the specified routes """

from flask import render_template

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

# Route for C
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

# Route for python
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

# Route for the integer
@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    return "{:d} is a number".format(n)

# Route for the number template
@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    return render_template('5-number.html', n=n)

# Route for the odd or even number
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
