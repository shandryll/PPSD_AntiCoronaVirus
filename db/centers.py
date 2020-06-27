import sqlite3

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