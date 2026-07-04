from backend.config.settings import settings


class ConfigService:

    @property
    def app_name(self):
        return settings.APP_NAME

    @property
    def app_version(self):
        return settings.APP_VERSION

    @property
    def database_url(self):
        return settings.DATABASE_URL

    @property
    def gemini_model(self):
        return settings.GEMINI_MODEL

    @property
    def debug(self):
        return settings.DEBUG


config = ConfigService()