
class User:

    def _create(self):
        command = (
            
            """ 
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    address TEXT,
                )
            """,
        )
        return command         

