#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import logging
from logging.handlers import RotatingFileHandler


from flask import abort, flash, Flask, render_template, redirect, request, url_for
#from flask_paginate import Pagination, get_page_parameter, get_page_args
from logging.config import fileConfig
import logging


from db.tables import *
from db.sql import *

import json
import requests
import datetime

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#

app = Flask(__name__)


'''
    *   Tenho que modificar os nomes das variaveis, mas na pressa nos testes
    *   Taquei o foda-se, e está funcionando... mas ainda irei mudar os nomes
'''
data_e_hora_atuais = datetime.datetime.now()
data_anterior = data_e_hora_atuais - datetime.timedelta(days=1)
data = data_e_hora_atuais.strftime('%Y%m%d')
d = data_anterior.strftime("%Y-%m-%d")
data_formatada = data_e_hora_atuais.strftime('%d/%m/%Y')


#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#
@app.route("/", methods=['GET', 'POST'])
def home():
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    #app.logger.info('ops')

    api = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/'+data+'?format=json'

    r = requests.get(api)

    print(api)
    
    dados = []

    if r.status_code == 200:
        reddit_data = json.loads(r.content)

    for i in reddit_data['data']:
        dados.append(i)

    informacoes = dados
    
    search = False
    q = request.args.get('q')
    if q:
        search = True

    return render_template('pages/home.html', data_atual = data_formatada, informacoes = informacoes)

@app.route("/suprimentos")
def suprimentos():
    data = all_supply_stores()

    return render_template('pages/suprimentos.html', data=data)


@app.route("/boletim")
def boletim():

    data = datetime.datetime.now()
    data_formatado = data.strftime('%Y-%m-%d')

    informacoes = []

    r = requests.get('https://brasil.io/api/dataset/covid19/boletim/data/?format=json')
    
    if r.status_code == 200:
        reddit_data = json.loads(r.content)

    # Obter as informacoes dos boletins do dia atual
    for info in reddit_data['results']:
        if info['date'] == data_formatado:
            informacoes.append(info)

    search = False
    q = request.args.get('q')
    if q:
        search = True

    return render_template('pages/boletim.html', informacoes=informacoes)


@app.route("/matriz")
def matriz():

    return render_template('forms/matriz.html', data=data)



@app.route('/centros', methods=['GET', 'POST'])
def centros():
    
    data = all_centers()

    return render_template('pages/centros_medicos.html', data=data)

#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)