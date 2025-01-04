from user.repository import select_user_by_email
from functools import wraps
from security.token import decode_token



def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
