from backend.auth.security import security


class AuthService:

    async def login(
        self,
        email: str,
        password: str
    ):

        # Temporary Authentication
        # JWT next step mein add hoga

        token = security.generate_token()

        return {
            "access_token": token,
            "token_type": "bearer"
        }


auth_service = AuthService()