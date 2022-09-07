from enum import Enum

class Error_Message(Enum):
    
    id_not_exist = "This user ID doesn't exist"
    user_not_exist = "This user doesn't exist"
    there_not_existent_users = "There are no registered users on this app"
    e_mail_already_exist = "This email address is already in use"
    nif_already_exist = "This NIF is used"
    negative_balance = "Amount greater than the account balance"
    equal_password = "Old and New password are the both the same"
    internal_error = "Server internal Error"
    admin_password_error = "The Admin Password do not match"
    withdrawal_not_exist = "This money withdrawal doesn't exist"
    there_not_withdrawals = "There are no registered withdrawals on this app"



def get_error(error_suf: str) -> str:
    return [
        error_message.value for error_name, error_message in Error_Message.__members__.items() 
            if error_name == f"{error_suf}_already_exist"
    ][0]
