from backend.agents.communication import communication
from backend.agents.message import AgentMessage


class AgentCoordinator:

    async def assign(
        self,
        sender: str,
        receiver: str,
        action: str,
        payload=None
    ):

        message = AgentMessage(
            sender=sender,
            receiver=receiver,
            action=action,
            payload=payload
        )

        return await communication.send(message)


coordinator = AgentCoordinator()