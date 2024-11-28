import jwt
from config import SECRET_KEY




async def create_token(user_data: dict):
    token = jwt.decode(user_data, SECRET_KEY, algorithm='HS256')
    return token

async def verify_token(token: str):
    info = jwt.decode(token, SECRET_KEY, algorithm='HS256')
    email = info['email']
    password = info['password']
    #тут надо логику обращения к базе данных и проверки данных
    if email == ... and password == ...:
        return #user_id
    else:
        return False