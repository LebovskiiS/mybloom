from passlib.context import CryptContext

hasher = CryptContext(schemes=["bcrypt"])

def password_hashing(password):
    hashed_password = hasher.hash(password)
    return  hashed_password






def verefy_password(password, hash_password):
    return hasher.verify(password, hash_password)