from backend.master.models import (
    AgentTask,
    AgentType
)


class MasterPlanner:

    def create_plan(self, message: str):

        text = message.lower()

        if "github" in text:
            return AgentTask(
                agent=AgentType.GITHUB,
                action="analyze"
            )

        if "browser" in text:
            return AgentTask(
                agent=AgentType.BROWSER,
                action="browse"
            )

        if "code" in text:
            return AgentTask(
                agent=AgentType.CODING,
                action="generate"
            )

        return AgentTask(
            agent=AgentType.CHAT,
            action="reply"
        )


planner = MasterPlanner()