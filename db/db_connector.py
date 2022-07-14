import os
import sqlite3
from termcolor import colored


# Create a function to connect to a database with SQLite
class SQLite_Connector:

    def __init__(self, db_name='db/bank_simulator.db') -> None:
        print(colored("[INFO] Start database connection", attrs=["bold"]))
        self.db_name = db_name
        self.connection = None
        self.sqlite_connect()
        self.cursor = self.connection.cursor()
        self.create_database()

    def create_database(self) -> None:
        sql_file = open("db/bank_simulator.sql")
        sql_as_string = sql_file.read()
        self.cursor.executescript(sql_as_string)

    def sqlite_connect(self) -> bool:
        """Connect to a database if exists. Create an instance if otherwise.
            Args:
                db_name: The name of the database to connect
            Returns:
                an sqlite3.connection object
        """
        try:
            # Create a connection
            conn = sqlite3.connect(self.db_name, check_same_thread=False)
        except sqlite3.Error:
            print(colored("[ERROR] Database not found", "red", attrs=["bold"]))
        finally:
            print(colored("[INFO] Database created", "blue", attrs=["bold"]))
            self.connection = conn    
    
    def execute_sql_query(self, query: str, apply_data_schema) -> list:
        results = self.cursor.execute(query)
        self.connection.commit()

        return apply_data_schema(results.fetchall())
    
    def close_db(self) -> None:
        self.connection.commit()
        self.connection.close()
       