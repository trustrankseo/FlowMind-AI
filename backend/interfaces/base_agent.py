from abc import ABC, abstractmethod


class BaseAgent(ABC):

    name = "agent"

    @abstractmethod
    async def handle(self, message):
        """Process an agent request."""
        raise NotImplementedError