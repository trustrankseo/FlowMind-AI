from backend.agents.coordinator import coordinator


class MasterDispatcher:

    async def dispatch(self, task):

        return await coordinator.assign(
            sender="master",
            receiver=task.agent.value,
            action=task.action,
            payload=task.payload
        )


dispatcher = MasterDispatcher()