
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