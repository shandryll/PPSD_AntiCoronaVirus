#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import abort, flash, Flask, render_template, redirect, request, url_for

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#
app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#
@app.route("/")
def home():
    return render_template('pages/home.html')

@app.route("/suprimentos")
def suprimentos():
    return render_template('pages/suprimentos.html')

#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)