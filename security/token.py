import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY


def create_token(email):
    payload = {'email':email,'exp':datetime.now() + timedelta(minutes=50*50*50)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def decode_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token
    except jwt.InvalidTokenError as e:
        raise e


