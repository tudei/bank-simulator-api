from cmath import pi
from controllers.user import User_Controller
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.error_message import Error_Message,get_error
from src.success_message import Success_Message

user_controller =  User_Controller()

class Withdrawal_Controller(SQLite_Connector):
    def __init__(self, db_name='database/bank_simulator.db') -> None:
        super().__init__(db_name)

    
    def get_money_withdrawal(self, id=None):

        money_withdrawals = None

        if id:
           money_withdrawals = self.execute_sql_query(f"SELECT * FROM  money_withdrawal WHERE id={id}", Schema.withdrawal)
        else:
            money_withdrawals = self.execute_sql_query(f"SELECT * FROM  money_withdrawal", Schema.withdrawal)
        
        if id and not money_withdrawals:
            return Schema.api_response(status=404,error_message=[
                Error_Message.withdrawal_not_exist.value,])
        elif not id and not money_withdrawals:
            return Schema.api_response(status=404,error_message=[
                Error_Message.there_not_withdrawals.value])
        return Schema.api_response(status=200,data = money_withdrawals)


    def create_new(self, id_user: int, amount: float, withdrawal_date:str ) -> list:

        user = user_controller.get_user(id_user)["data"][0]
        print(user)
       
        if not user:
            return Schema.api_response(status=404, error_message=[
                Error_Message.user_not_exist.value]
            )
        
        if user["balance"] < amount:
            return Schema.api_response(status=200, error_message=[
                Error_Message.negative_balance.value]
            )

        new_user_balance = user["balance"] - amount
        user_controller.update_user_balance(user["account_number"], new_user_balance)

        sql_query = f"""
            INSERT INTO money_withdrawal  
                (id_user, amount, withdrawal_date)
            VALUES 
                ({id_user},{amount},'{withdrawal_date}');
        """
        try:
            self.execute_sql_query(sql_query,Schema.withdrawal)
        except Exception as error:
            error_suf = f"{error}".split(".")
            return Schema.api_response(
                status=500,
                error_message=[f"{get_error(error_suf[1])}"]
            )

        new_money_withdrawal = self.get_money_withdrawal()["data"][-1]
        return Schema.api_response(
                status=200,
                data=new_money_withdrawal,
                success_message=[Success_Message.new_withdrawal.value]
            )
        