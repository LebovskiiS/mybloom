from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from exception import SecurityError
from user.repository import select_user_by_email
from security.token import decode_token
from data_base.postgres import get_session


security = HTTPBearer()

def get_jwt_from_header(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Optional[str]:
    if not credentials:
        raise SecurityError(status_code=401, message="Missing authorization credentials")
    if credentials.scheme.lower() != "bearer":
        raise SecurityError(status_code=401, message="Invalid authorization scheme")
    return credentials.credentials


async def get_current_user(token: str = Depends(get_jwt_from_header), session: AsyncSession = Depends(get_session)):
    jwt = decode_token(token)
    email = jwt['email']
    user_data = await select_user_by_email(email, session)
    if not user_data.name:
        raise SecurityError(status_code=403, message= 'Missing authorization credentials')
    return user_data