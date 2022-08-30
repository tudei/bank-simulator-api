from controllers.user import User_Controller
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema

user_controller =  User_Controller()

class Withdrawal_Controller(SQLite_Connector):
    def __init__(self, db_name='database/bank_simulator.db') -> None:
        super().__init__(db_name)

    
    def get_withdrawal(self, id=None):
        if id:
            return self.execute_sql_query(f"SELECT * FROM  money_withdrawal WHERE id={id}", Schema.withdrawal)
        
        return self.execute_sql_query(f"SELECT * FROM  money_withdrawal", Schema.withdrawal)

    def create_new(self, id_user: int, amount: float, withdrawal_date:str ) -> list:

        withdrawal_status = self.withdrawal_amount(id_user,amount)

        if not withdrawal_status:
            print("levantamento regeitado")
            return []

        sql_query = f"""
            INSERT INTO money_withdrawal  
                (id_user, amount, withdrawal_date)
            VALUES 
                ({id_user},{amount},'{withdrawal_date}');
        """
        self.execute_sql_query(sql_query,Schema.withdrawal)

        return self.get_withdrawal()[-1]

    def withdrawal_amount(self, id_user, amount) -> bool:
        user = user_controller.get_user(id_user)[0]

        if not user:
            return False

        if user["balance"] < amount:
            return False  

        new_user_balance = user["balance"] - amount
        user_controller.update_user_balance(user["account_number"], new_user_balance)

        return True
        