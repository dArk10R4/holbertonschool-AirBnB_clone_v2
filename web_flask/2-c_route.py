#!/usr/bin/python3
"""Python script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)