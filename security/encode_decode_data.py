from config import SECRET_KEY
from cryptography.fernet import Fernet



def encode_data(data: str) -> str:
    try:
        cipher = Fernet(SECRET_KEY.encode())
        encrypted_data = cipher.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        raise ValueError(f"Error during data encoding: {e}")


def decode_data(encoded_data: str) -> str:
    try:
        cipher = Fernet(SECRET_KEY.encode())
        decrypted_data = cipher.decrypt(encoded_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        raise ValueError(f'Invalid encrypted data or key. Decryption failed {e}.')