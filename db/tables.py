#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
#from ..server.log import log
import sqlite3


#----------------------------------------------------------------------------#
# Initial Data
#----------------------------------------------------------------------------#
def create_table():
    
    #log.gravar('Criando o banco de dados')

    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    commands = (
    
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
                available_supplies TEXT
            )
        
        """,
    )

    for c in commands:
        #log.gravar('Comando executado: ', c)
        cursor.execute(c)
        
    #log.gravar('Tabelas Criadas!')
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
        #log.gravar('Comando executado: ', command)
        cursor.execute(command)
        db.commit()

    #log.gravar('Banco de dados, Ok!')        



def initial_centers():
    comandos = (
        
        """
            INSERT INTO health_centers (name, opening_hours, address, phone, test_available) 
            
            VALUES (
                'Teste1', 'xxxx', 'teste', '31 999999', 'sim'
            )

        """,

         """
            INSERT INTO health_centers (name, opening_hours, address, phone, test_available) 
            
            VALUES (
                'Teste2', 'sdsdfxxxx', 'teste2', '(31) 9222222','daddsfsdfsdsr'
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