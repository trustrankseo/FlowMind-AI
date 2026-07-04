from backend.providers.gemini import GeminiProvider
from backend.providers.openai import OpenAIProvider


class ProviderManager:

    def __init__(self):

        self.providers = {
            "gemini": GeminiProvider(),
            "openai": OpenAIProvider(),
        }

        self.active_provider = "gemini"

    def set_provider(self, name: str):

        if name in self.providers:
            self.active_provider = name

    def get_provider(self):

        return self.providers[self.active_provider]


provider_manager = ProviderManager()