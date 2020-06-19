#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import abort, flash, Flask, render_template, redirect, request, url_for

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
@app.route("/")
def home():
    r = requests.get('https://brasil.io/api/dataset/covid19/boletim/data/?format=json')
    
    if r.status_code == 200:
        reddit_data = json.loads(r.content)

    """
        Data:
        UF/Link para Boletim:
        Observação:
    """
    for boletim in reddit_data['results']:
        print(
            
            "Data: ", boletim['date'],
            "\nUF/Link para Boletim:", boletim['state'],
            "\nObservação:", boletim['notes'], 
            "\nLink: ", boletim['url'],
            "\n----------------------------------",
            "\n"
        )

    #print (reddit_data['results'])

    return render_template('pages/home.html')

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