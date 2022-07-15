
class Schema:
    
    @staticmethod
    def user(data: tuple) -> list:
        
        return [
            {
                "id": dt[0],
                "first_name": dt[1],
                "last_name": dt[2],
                "age": dt[3],
                "e_mail": dt[4],
                "nif": dt[5],
                "code": dt[6],
                "user_password": dt[7],
                "balance": dt[8],
                "account_number": dt[9], 
                "user_type": dt[10],
            } for dt in data]
    
    @staticmethod
    def tranfer(data: tuple) -> list:
        
        return [
            {
                "id": dt[0],
                "id_sender":dt[1],
                "id_receiver":dt[2],
                "amount":dt[3],
                "transfer_date":dt[4], 
                "transfer_code ":dt[5],      
            } for dt in data]
    
    @staticmethod
    def api_response(status: int, success_message: list, error_message: list, data: list) -> list:
        
        return {
            "status": status,
            "success_message": [{index: message} for index, message in enumerate(success_message)],
            "error_message": [{index: error} for index, error in enumerate(error_message)],
            "data": data
        }
 