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

        return await agent.handle(message)


communication = AgentCommunication()