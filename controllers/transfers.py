from db.db_connector import SQLite_Connector
from schemas.schemas import Schema



class Transfers_Controller(SQLite_Connector):

    def __init__(self, db_name='db/bank_simulator.db') -> None:
        super().__init__(db_name)

    def get_user(self, id=None) -> list:
        if id:
            return self.execute_sql_query(f"SELECT * FROM money_transfer WHERE id={id}", Schema.tranfer) 
        return self.execute_sql_query(f"SELECT * FROM money_transfer", Schema.tranfer)      

    
    def create_new(self, id_sender: int, id_receiver: int ,amount: float, 
                    transfer_date: str, transfer_code:str) -> list:
        sql_query = f"""
                    INSERT INTO money_transfer(
                       id_sender, id_receiver, amount, transfer_date, transfer_code
                    )VALUES({id_sender},{id_receiver},{amount},
                    '{transfer_date}','{transfer_code}')
        """
        self.execute_sql_query(sql_query, Schema.tranfer)
        return
