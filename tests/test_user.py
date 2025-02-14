import time
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine

from models import Base
import pytest
from fastapi.testclient import TestClient
from main import app
from httpx import AsyncClient



#test engine
test_engine = create_async_engine('sqlite+aiosqlite://:memory:')





client = TestClient(app)

def test_h_w():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"response":"Hello world"}


reg_data = {
        "name": "tesq4t",
        "surname": "tqe4st",
        "email": "tewst54@gmail.com",
        "phone": "111w141111",
        "password": "testpassword",
        "address": "testaddress"}



def test_registration():
    response = client.post('/user/registration', json=reg_data)
    assert response.status_code == 200
    assert response.json()['message'] == 'login success'
    assert response.json()['jwt'] is not None

