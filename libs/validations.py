# validations.py

from configs.secrets import valid_user_id

def check_user_id(message):
    return message.from_user and message.from_user.id == valid_user_id
