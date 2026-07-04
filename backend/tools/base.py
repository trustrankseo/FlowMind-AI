from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = "base"

    description = ""

    @abstractmethod
    async def execute(self, **kwargs):
        pass