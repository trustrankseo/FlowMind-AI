from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = "tool"

    @abstractmethod
    async def execute(self, request):
        """Execute a tool request."""
        raise NotImplementedError