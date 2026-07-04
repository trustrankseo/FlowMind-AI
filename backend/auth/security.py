from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from backend.auth.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class SecurityManager:

    def hash_password(
        self,
        password: str
    ):

        return pwd_context.hash(password)

    def verify_password(
        self,
        password: str,
        hashed: str
    ):

        return pwd_context.verify(
            password,
            hashed
        )

    def create_access_token(
        self,
        subject: str
    ):

        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload = {
            "sub": subject,
            "exp": expire
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )


security = SecurityManager()