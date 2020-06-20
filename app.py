#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import abort, flash, Flask, render_template, redirect, request, url_for
from flask_paginate import Pagination, get_page_parameter

from db.tables import *
from db.sql import *

import json
import requests

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#
app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#
@app.route("/", methods=['GET', 'POST'])
def home():
    r = requests.get('https://brasil.io/api/dataset/covid19/boletim/data/?format=json')
    
    if r.status_code == 200:
        reddit_data = json.loads(r.content)

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(reddit_data['results']), search=search)

    return render_template('pages/home.html', informacoes=reddit_data['results'], pagination=pagination)

@app.route("/suprimentos")
def suprimentos():
    data = all_supply_stores()

    return render_template('pages/suprimentos.html', data=data)



@app.route('/centros', methods=['GET', 'POST'])
def centros():
    
    data = all_centers()

    return render_template('pages/centros_medicos.html', data=data)

#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)