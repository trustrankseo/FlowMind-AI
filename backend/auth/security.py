from datetime import datetime, timedelta
import secrets


class SecurityManager:

    def generate_token(self):

        return secrets.token_urlsafe(32)

    def expires_at(self, hours: int = 24):

        return datetime.utcnow() + timedelta(hours=hours)


security = SecurityManager()