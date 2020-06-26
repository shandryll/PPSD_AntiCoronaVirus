#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import logging
from logging.handlers import RotatingFileHandler


from flask import abort, flash, Flask, render_template, redirect, request, url_for, session
#from flask_paginate import Pagination, get_page_parameter, get_page_args

from db.tables import *
from db.sql import *
from db.users import *
from db.centers import *

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
d = data_anterior.strftime("%Y%m%d")
data_formatada = data_e_hora_atuais.strftime('%d/%m/%Y')


#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#
@app.route("/", methods=['GET', 'POST'])
def home():

    api = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/'+data+'?format=json'

    r = requests.get(api)

    print('\nLink da API: ', api)
    
    dados = []

    if r.status_code == 200:
        reddit_data = json.loads(r.content)
        
        '''
            * Condicional verificando o tamanho do retorno do conteudo
            * que busca informações do dia atual, caso não possua nenhum
            * dado, ele busca o do dia anterior
        '''
        
        if(len(reddit_data['data']) == 0):
            api = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/'+d+'?format=json'

            r = requests.get(api)

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
    d = data_anterior.strftime("%Y-%m-%d")

    informacoes = []

    r = requests.get('https://brasil.io/api/dataset/covid19/boletim/data/?format=json')
    
    if r.status_code == 200:
        reddit_data = json.loads(r.content)

    # Obter as informacoes dos boletins do dia atual
    for info in reddit_data['results']:
        if info['date'] == d:
            informacoes.append(info)

    search = False
    q = request.args.get('q')
    if q:
        search = True

    return render_template('pages/boletim.html', informacoes=informacoes)


@app.route("/check_my_situation", methods=['GET', 'POST'])
def matriz():

    if request.method == 'GET':
        return render_template('forms/cadastro.html')

    elif request.method == 'POST':
        
        user_name = request.form["name"]
        user_addres = request.form["endereco"]
        user_region = request.form["regiao"]
        user_covid = request.form["covid"]
        user_prevention = request.form["prevencao"]

        print(
            '\nNome: ', user_name,
            '\nEndereco: ', user_addres,
            '\nRegiao: ', user_region,
            '\nConvive com alguem infectado? ', user_covid,
            '\nSegue o padrão de prevenção? ', user_prevention
        )

        data = [user_name, user_addres, user_region, user_covid, user_prevention]
        user = verify_user(data)
        
        if user == []:
            print('\nInserindo usuario')

            insert_user(data)

            return redirect(url_for('home'))

        else:
            print('\nVerificando a situação do usuario ')

            user = verify_situation_user(data)

            for i in user:
                print('\nUser: ', i)

            return render_template('pages/my_situation.html', data = user)


# URL para verificar se o Usuario está infectado com o Covid
@app.route('/my_situation', methods=['GET', 'POST'])
def my_situation():            
    

    return render_template('pages/my_situation.html', data=user)



@app.route('/centros', methods=['GET', 'POST'])
def centros():
    
    data = all_centers()

    return render_template('pages/centros_medicos.html', data=data)

#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)