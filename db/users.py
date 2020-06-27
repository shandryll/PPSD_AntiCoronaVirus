import sqlite3

# Verifica se possui algum registro do usuario no banco
def verify_user(data):    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]
    user_addres = data[1]
    user_region = data[2]

    cursor.execute(f'SELECT * FROM users WHERE name = "{user_name}" AND uf = "{user_region}"')
    
    data = cursor.fetchall()
    db.close()
    
    return data


def insert_user(data):
    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    # Dados obtidos pelo form
    name = data[0]
    address = data[1]
    state = data[2]
    covid_person = data[3]
    detachment = data[4]
    without_mask = data[5]
    hand_hygiene = data[6]
    
    # Por default será inserido que ele não está infectado pela covid
    Im_infected = "Não"  

    cursor.execute(f"""
        INSERT INTO users (name, address, uf, coexists_covid_person, detachment,
        without_mask, hand_hygiene, Im_infected) 
            
            VALUES (
                "{name}", 
                "{address}", 
                "{state}",
                "{covid_person}",
                "{detachment}",
                "{without_mask}",
                "{hand_hygiene}",
                "{Im_infected}"
            )
        """
    )
    
    db.commit()
    db.close()

    
def verify_situation_user(data):
    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]

    cursor.execute(
        f'SELECT uf, coexists_covid_person, detachment, without_mask, hand_hygiene FROM users WHERE name = "{user_name}"'
    )
    
    data = cursor.fetchall()
    db.close()
    
    return data


# Metodo que altera o status do usuario, colocando como infectado
def update_infected_user(data):
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]

    cursor.execute(
        f'UPDATE users SET Im_infected = "Sim" FROM users WHERE name = "{user_name}"'
    )
    
    db.commit()
    db.close()
    
    return data


def check_user(data):
    
    covid = data[3] # Vive com alguém com COVID?
    detachment = data[4] # Segue o Distanciamento Social?
    without_mask = data[5] # Você sai de casa sem a mascara?
    hand_hygiene = data[6] # Você higieniza a sua mão com frequencia?

    if covid == "Sim" and detachment == "Não" and without_mask == "Sim" and hand_hygiene == "Não":        
        update_infected_user(data)                

