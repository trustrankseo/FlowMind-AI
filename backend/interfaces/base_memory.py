from abc import ABC, abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    async def load(self, session_id: str):
        """Load memory."""
        raise NotImplementedError

    @abstractmethod
    async def save(self, session_id: str, role: str, content: str):
        """Save memory."""
        raise NotImplementedError