from config import SECRET_KEY
from cryptography.fernet import Fernet



def encode_data(data: str, secret_key: str) -> str:
    cipher = Fernet(secret_key.encode())
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()


def decode_data(encoded_data: str, secret_key: str) -> str:
    try:
        cipher = Fernet(secret_key.encode())
        decrypted_data = cipher.decrypt(encoded_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        raise ValueError("Invalid encrypted data") from e