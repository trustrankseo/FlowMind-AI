from abc import ABC, abstractmethod


class BasePlugin(ABC):

    name = "plugin"

    version = "1.0.0"

    @abstractmethod
    async def setup(self):
        pass