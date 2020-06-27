#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import sqlite3


#from centers import *
#import users

#----------------------------------------------------------------------------#
# Initial Data
#----------------------------------------------------------------------------#
def create_table():

    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    commands = (
        
        """ 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                uf TEXT,
                coexists_covid_person TEXT,
                detachment TEXT,
                without_mask TEXT,
                hand_hygiene TEXT,
                Im_infected TEXT
            )
        """,

        """ 
            CREATE TABLE IF NOT EXISTS health_centers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                opening_hours TEXT,
                address TEXT,
                phone TEXT,
                test_available TEXT
            )
        
        """,

        """ 
            CREATE TABLE IF NOT EXISTS supply_stores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                site TEXT,
                available_supplies TEXT,
                quantity INTEGER
            )
        
        """,
    )

    for c in commands:
        cursor.execute(c)
        
    print('Tabelas Criadas!')
    initial_data()
    db.close()



def initial_data():

    #log.gravar('Iniciando o Banco...')

    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    commands = (
        
       initial_centers() + initial_supply_stores()
    )

    for command in commands:
        cursor.execute(command)
        db.commit()
        

def initial_centers():
    comandos = (
        
        """
            INSERT INTO health_centers (name, opening_hours, address, phone, test_available) 
            
            VALUES (
                'Centro de Saúde Bairro das Indústrias', 
                '7 às 19h', 
                'Rua Maria de Loudes Manso, 80, Bairro das Indústrias', 
                '3277-5978 | 3277-5899', 
                'Não'
            )

        """,

         """
            INSERT INTO health_centers (name, opening_hours, address, phone, test_available) 
            
            VALUES (
                'Centro de Saúde Bonsucesso', 
                '7 às 19h', 
                'Av. Dr. Cristiano Machado Resende, 1875', 
                '3277-9069 | 3277-9132',
                'Não'
            )

        """,
    )

    return comandos
    
def initial_supply_stores():
    comandos = (

        """
            INSERT INTO supply_stores (name, address, site, available_supplies) 
            
            VALUES (
                'Loja de Suprmentos 1', 'teste', 'http://teste', 'alcool em gel'
            )

        """,
    )

    return comandos

#----------------------------------------------------------------------------#
# Launch
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    create_table()