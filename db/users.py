import sqlite3

def verify_user(data):
    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    user_name = data[0]
    user_addres = data[1]
    user_region = data[2]

    cursor.execute(f'SELECT * FROM users WHERE name = "{user_name}" AND region = "{user_region}"')
    
    data = cursor.fetchall()
    db.close()
    
    return data

def insert_user(data):
    
    db = sqlite3.connect('anti_covid.db')
    cursor = db.cursor()
    
    name = data[0]
    address = data[1]
    region = data[2]
    covid_person = data[3]
    prevention = data[4]
    Im_infected = False  

    cursor.execute(f"""
        INSERT INTO users (name, address, region, coexists_covid_person, Im_infected, prevention) 
            
            VALUES (
                "{name}", 
                "{address}", 
                "{region}",
                "{covid_person}",
                "{Im_infected}",
                "{prevention}"
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
        f'SELECT region, coexists_covid_person, prevention FROM users WHERE name = "{user_name}"'
    )
    
    data = cursor.fetchall()
    db.close()
    
    return data

