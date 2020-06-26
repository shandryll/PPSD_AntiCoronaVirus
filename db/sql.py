import sqlite3


#----------------------------------------------------------------------------#
# CRUD
#----------------------------------------------------------------------------#
def all_centers():
    print('Selecionando todos os centros medicos')

    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM health_centers')
    data = cursor.fetchall()
    db.close()

    return data


def all_supply_stores():
    print('Selecionando todos as lojas que vendem suprimentos')

    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM supply_stores')
    data = cursor.fetchall()
    db.close()

    return data    



