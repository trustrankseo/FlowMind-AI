from abc import ABC, abstractmethod


class BaseProvider(ABC):

    name = "provider"

    @abstractmethod
    async def chat(self, prompt: str):

        raise NotImplementedError