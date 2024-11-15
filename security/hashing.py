import hashlib


async def password_hashing(password):
    hashed_password = hashlib.sha256(password, usedforsecurity= True)
    return  hashed_password






async def is_password_match(db_pass, input_pass):
    hashed_password = hashlib.sha256(input_pass, usedforsecurity=True)
    if hashed_password == db_pass:
        return True
    else:
        return False