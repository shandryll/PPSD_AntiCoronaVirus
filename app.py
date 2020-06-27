#!/usr/bin/python

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import abort, flash, Flask, render_template, redirect, request, url_for

from db.sql import *
from db.users import *
from db.centers import *
from server.log import *
from server.api import *

import json
import requests
import datetime

#----------------------------------------------------------------------------#
# App Config
#----------------------------------------------------------------------------#

app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#
@app.route("/", methods=['GET', 'POST'])
def home():

    informacoes = state_situations()
    
    search = False
    q = request.args.get('q')
    if q:
        search = True

    return render_template('pages/home.html', data_atual = data_formatada, informacoes = informacoes)


# Lista as lojas com os produtos que ajuda a combater a doença
@app.route("/suprimentos")
def suprimentos():
    data = all_supply_stores()

    return render_template('pages/suprimentos.html', data=data)


# Busca dados de cada estado, esses dados obtidas por uma API
@app.route("/boletim")
def boletim():

    informacoes = get_boletins_anterior()

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
        user_region = request.form["uf"]
        user_covid = request.form["covid"]
        user_prevention = request.form["distanciamento"]
        user_mask = request.form["sem_mascara"]
        user_higiene = request.form["higiene_mao"]

        # Para imprimir no console, ajuda para a realização de testes
        gravar(
            'Dados informados pelo usuario: '+
            '\n\tNome: ' + user_name+
            '\n\tEndereco: ' + user_addres+
            '\n\tRegiao: '+ user_region+
            '\n\tConvive com alguem infectado? '+ user_covid+
            '\n\tSegue o padrão de prevenção? '+ user_prevention
        )

        data = [
            user_name, user_addres, 
            user_region, user_covid, 
            user_prevention, user_mask,
            user_higiene
        ]
        
        user = verify_user(data)
        
        if user == []:
            gravar('Inserindo novo Usuario')
            
            insert_user(data)
            
            user = verify_user(data)
            
            return render_template('pages/my_situation.html', data = user)    

        else:
            gravar('Usuario existente no banco, verificando o status')
            
            verify_situation_user(data)
    

            return render_template('pages/my_situation.html', data = user)

        



@app.route('/centros', methods=['GET', 'POST'])
def centros():

    gravar('Buscandos todos os dados de centros medicos')
    data = all_centers()
    return render_template('pages/centros_medicos.html', data=data)


#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)
