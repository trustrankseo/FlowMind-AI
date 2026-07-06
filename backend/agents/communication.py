from backend.agents.registry import agent_registry


class AgentCommunication:

    async def send(self, message):

        agent = agent_registry.get(
            message.receiver
        )

        if agent is None:
            return {
                "success": False,
                "error": "Agent not found"
            }

        # Agents receive the payload (the actual task data), not the
        # AgentMessage envelope itself — the envelope (sender/receiver/
        # action) is routing metadata, not something an agent's `handle()`
        # should need to unpack.
        return await agent.handle(message.payload)


communication = AgentCommunication()