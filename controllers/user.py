from db.db_connector import SQLite_Connector
from schemas.schemas import Schema

import random


class User_Controller(SQLite_Connector):

    def __init__(self) -> None:
        super().__init__()
    
    def get_user(self, id=None) -> list:
        if id:
            return self.execute_sql_query(f"SELECT * FROM user WHERE id={id}", Schema.user)
        
        return self.execute_sql_query(f"SELECT * FROM user", Schema.user)
    
    def verify_account_number(self, nr_account: int) -> bool:
        all_user = self.get_user()
    
    def generate_account_number(self) -> int:
        return random.randint(1000000000, 99999999999)
    
    def create_new(self, first_name: str, last_name: str, age: int, e_mail: str, 
                    balance: float, nif: int, user_password: str, user_type="Stander") -> list:
        sql_query = f"""
            INSERT INTO user (
                first_name, last_name, age, e_mail, nif, 
                code, user_password, balance, account_number, user_type
            ) VALUES (
                '{first_name}', '{last_name}', {age}, '{e_mail}', {nif}, 
                {random.randint(1000, 9999)}, '{user_password}', {balance}, 
                {self.generate_account_number()}, '{user_type}'
            ); 
            """
        self.execute_sql_query(sql_query, Schema.user)
        return self.get_user()[0]
    
    def delete_user(self, id: int) -> bool:
        sql_query = f""" DELETE FROM user WHERE id={id}"""
        self.execute_sql_query(sql_query, Schema.user)

        
    def update_user_password(self, new_password: str) -> bool:
        sql_query = f"""
            UPDATE user SET user_password='{new_password}'
            WHERE id={id}
            """
        self.execute_sql_query(sql_query)
    
    def update_user_balance(self, account_number: int, balance: float) -> bool:
        sql_query = f"""
        UPDATE user SET balance = {balance} 
        WHERE account_number={account_number}
        """
        self.execute_sql_query(sql_query, Schema.user)
