"""Main application."""

import os
from flask import Flask, render_template, request

app = Flask(__name__)


###
# Routing
###

@app.route('/')
def home():
    """Render the actual cv page."""
    return render_template('home.html')


###
# General functions
###

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
