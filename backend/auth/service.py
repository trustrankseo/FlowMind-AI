from backend.auth.security import security


class AuthService:

    async def login(
        self,
        email: str,
        password: str
    ):

        # Temporary User Validation
        # Database validation next sprint

        token = security.create_access_token(
            email
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }


auth_service = AuthService()