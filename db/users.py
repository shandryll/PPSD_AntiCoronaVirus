import sqlite3

# Verifica se possui algum registro do usuario no banco
def verify_user(data):    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]
    print('Verificando o cadasto do Usuario: ', user_name)

    cursor.execute(f'SELECT * FROM users WHERE name = "{user_name}" ')
    
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
    
    im_infected = verify_im_infected(detachment, without_mask, hand_hygiene)  

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
                "{im_infected}"
            )
        """
    )
    
    db.commit()
    db.close()

    
def verify_situation_user(data):
    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]
    print('Usr name: ', user_name)

    cursor.execute(
        f'SELECT detachment, without_mask, hand_hygiene FROM users WHERE name = "{user_name}"'
    )
    
    data = cursor.fetchall()
    
    check_user(data, user_name)
    
    db.close()



# Metodo que altera o status do usuario, colocando como infectado
def update_infected_user(data, name):
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = name
    print('nome: ', user_name)

    cursor.execute(
        f'UPDATE users SET Im_infected = "Sim" WHERE name = "{user_name}"'
    )
    
    db.commit()
    
    


def check_user(data, name):

    #covid = data[4] # Vive com alguém diagnosticado com COVID?
    print(data)

    detachment = data[0][0] # Segue o Distanciamento Social?
    without_mask = data[0][1] # Você sai de casa sem a mascara?
    hand_hygiene = data[0][2] # Você higieniza a sua mão com frequencia?

    print('Dist: '+ detachment + " sem mascara: "+ without_mask+ " higiene mao: "+ hand_hygiene)

    if verify_im_infected(detachment, without_mask, hand_hygiene) == "Sim":
        print('aki')
        update_infected_user(data, name)

    return data                     


def verify_im_infected(detachment, without_mask, hand_hygiene):
    
    if detachment == "Não" and without_mask == "Sim" and hand_hygiene == "Não":        
        return "Sim" # Está infectado

    return "Não"
