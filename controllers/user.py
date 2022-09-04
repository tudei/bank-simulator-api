from regex import R
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.error_message import Error_Message, get_error
from src.success_message import Success_Message

import random


class User_Controller(SQLite_Connector):

    def __init__(self) -> None:
        super().__init__()

    def get_user(self, id=None) -> list:
        users = None
        if id:
            users = self.execute_sql_query(
                f"SELECT * FROM user WHERE id={id}", Schema.user)
        else:
            users = self.execute_sql_query(f"SELECT * FROM user", Schema.user)

        if id and not users:
            return Schema.api_response(status=200, error_message=[
                Error_Message.user_not_exist.value])
        elif not id and not users:
            return Schema.api_response(status=200, 
                error_message=Error_Message.there_not_existent_users.value)
        return Schema.api_response(status=200, data=users)

    def verify_account_number(self, nr_account: int) -> bool:
        all_user = self.get_user()

    def generate_account_number(self) -> int:
        return random.randint(1000000000, 99999999999)

    def create_new(self, first_name: str, last_name: str, age: int, e_mail: str,
                   balance: float, nif: int, user_password: str, user_type="Stander") -> list:

        sql_query = f"""
            INSERT INTO user (
                first_name, last_name, age, e_mail, nif, code, user_password, 
                balance, account_number, user_type, account_state
            ) VALUES (
                '{first_name}', '{last_name}', {age}, '{e_mail}', {nif}, 
                {random.randint(1000, 9999)}, '{user_password}', {balance}, 
                {self.generate_account_number()}, '{user_type}', 1
            ); 
            """

        try:
            self.execute_sql_query(sql_query, Schema.user)
        except Exception as error:
            error_suf = f"{error}".split(".")
            return Schema.api_response(
                status=500,
                error_message=[f"{get_error(error_suf[1])}"]
            )

        new_user = self.get_user()[-1]

        return Schema.api_response(
            status=200,
            data=new_user,
            success_message=[Success_Message.new_user.value]
        )

    def delete_user(self, id: int, admin_password: str) -> bool:
        user = self.get_user(id)
        if user["user_password"] == admin_password:
            sql_query = f""" DELETE FROM user WHERE id={id}"""
            return Schema.api_response(
                status=200,
                data=self.execute_sql_query(sql_query, Schema.user),
                success_message=[Success_Message.deleted_user]
            )

        return Schema.api_response(
            status=503,
            error_message=[Error_Message.admin_password_error]
        )

    def update_user_password(self, id: int, new_password: str) -> bool:
        sql_query = f"""
            UPDATE user SET user_password='{new_password}'
            WHERE id={id}
            """
        return self.execute_sql_query(sql_query, Schema.user)

    def update_user_balance(self, account_number: int, balance: float) -> bool:
        sql_query = f"""
        UPDATE user SET balance = {balance} 
        WHERE account_number={account_number}
        """
        return self.execute_sql_query(sql_query, Schema.user)
