from backend.providers.factory import factory
from backend.providers.gemini import gemini_provider


class ProviderManager:

    def __init__(self):

        factory.register(
            "gemini",
            gemini_provider
        )

        self.active = "gemini"

    def get_provider(self):

        return factory.get(
            self.active
        )

    def set_provider(
        self,
        name: str
    ):

        if factory.get(name):

            self.active = name


provider_manager = ProviderManager()