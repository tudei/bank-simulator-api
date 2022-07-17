import random


from db.db_connector import SQLite_Connector
from schemas.schemas import Schema
from controllers.user import User_Controller

user_controller =  User_Controller()

class Transfers_Controller(SQLite_Connector):

    def __init__(self, db_name='db/bank_simulator.db') -> None:
        super().__init__(db_name)

    def get_transfers(self, id=None) -> list:
        if id:
            return self.execute_sql_query(f"SELECT * FROM money_transfer WHERE id={id}", Schema.tranfer) 
        return self.execute_sql_query(f"SELECT * FROM money_transfer", Schema.tranfer)      

    
    def create_new(self, id_sender: int, account_number: int ,amount: float, 
                    transfer_date: str) -> list:

        transfer_status = self.transfer_amount(id_sender, account_number, amount)

        if not transfer_status:
            return []

        transfer_code = str(random.randint(1000000000, 99999999999))

        sql_query = f"""
                    INSERT INTO money_transfer(
                       id_sender, account_number, amount, transfer_date, transfer_code
                    )VALUES({id_sender},{account_number},{amount},
                    '{transfer_date}','{transfer_code}')
        """
        self.execute_sql_query(sql_query, Schema.tranfer)

        return self.get_transfers()[-1]
    
    def transfer_amount(self, id_sender: int, account_number: int, amount: float) -> bool:
        sender = user_controller.get_user(id_sender)[0]
        reciver = user_controller.get_user_by_account_number(account_number)[0]

        if not sender :
            #messagm de erro /type erro
            return False
        if not reciver:
            #messagem de erro /type erro
            return False

        if sender["balance"] < amount:
            #messagem de erro /type erro
            return False  
        new_sender_balance = sender["balance"] - amount 
        new_reciver_balance = reciver["balance"] + amount
        
        user_controller.update_user_balance(sender["account_number"], new_sender_balance)
        user_controller.update_user_balance(reciver["account_number"], new_reciver_balance)

        return True
    
    


    