from enum import Enum

class Error_Message(Enum):
    
    id_not_exist = "This user ID doesn't exist"
    e_mail_already_exist = "This email address is already in use"
    nif_already_exist = "This NIF is used"
    negative_balance = "Amount grather than the account balance"
    equal_password = "Old and New password are the both the same"
    internal_error = "Server internal Error"
    admin_password_error = "The Admin Password do not match"


def get_error(error_suf: str) -> str:
    return [
        error_message.value for error_name, error_message in Error_Message.__members__.items() 
            if error_name == f"{error_suf}_already_exist"
    ][0]
