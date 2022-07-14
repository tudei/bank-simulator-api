import sqlite3


# Create a function to connect to a database with SQLite
class SQL_Connector:

    def __init__(self, db_name='sample.db') -> None:

        self.db_name = db_name
        self.connection = self.sqlite_connect()
        self.cursor = self.connection.cursor()

    def sqlite_connect(self):
        """Connect to a database if exists. Create an instance if otherwise.
        Args:
            db_name: The name of the database to connect
        Returns:
            an sqlite3.connection object
        """
        try:
            # Create a connection
            conn = sqlite3.connect(self.db_name)
        except sqlite3.Error:
            print(f"Error connecting to the database '{self.db_name}'")
        finally:
            return conn
        
    def create_database(self):

        sql_create_table_query = """
            CREATE TABLE pessoa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                BI INT NOT NULL, 
                nome VARCHAR(100) NOT NULL,
                genero VARCHAR(50),
                zona VARCHAR(255),
                telefone INT NOT NULL,
                email VARCHAR(255),
                data_nascimento VARCHAR(255),
                vacina VARCHAR(255),
                numero_dose INT NOT NULL,
                obs VARCHAR(255)
            );"""

        self.cursor.execute(sql_create_table_query)
        self.connection.commit()
    
    def delete_db(self) -> None:
        self.cursor.execute("""
            DROP TABLE pessoa; 
        """)
        self.connection.commit()
    
    def insert_in_db(
        self, bi: int, nome: str, genero: str, zona: str, telefone: int, email: str, 
        data_nascimento: str, vacina: str, numero_dose: str, obs: str) -> None:

        sql_query = f"""
            INSERT INTO pessoa (
                bi, nome, genero, zona, telefone, email, data_nascimento, vacina, numero_dose, obs)
            VALUES (
                {bi}, '{nome}', '{genero}', '{zona}', {telefone}, '{email}', '{data_nascimento}', 
                '{vacina}', '{numero_dose}', '{obs}'); 
        """
        self.cursor.execute(sql_query)
        self.connection.commit()
    
    def get_users(self, id=None) -> None:
            
        results = self.cursor.execute("""SELECT * FROM pessoa;""")

        self.connection.commit()

        if not id:
            return results.fetchall()
        
        return self.get_specific_user(results.fetchall(), id)

    def get_specific_user(self, results: list, user_id: int) -> tuple:
        for user in results:
            if user[0] == user_id:
                return user
            
        return None
    
    def close_db(self) -> None:
        self.connection.commit()
        self.connection.close()
    
db = SQL_Connector()
# db.delete_db()
db.create_database()
db.insert_in_db(1454145, "nome_2", "genero", "zona", 34523433, "email@gmail.com", 
        "22/06/2022", "vacina", 2, "obs")
users = db.get_users() # get all users
print(users)
# user = db.get_users(2) # get a specific user