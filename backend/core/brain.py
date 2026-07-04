from backend.agents.manager import manager


class Brain:

    def think(self, message: str):

        text = message.lower()

        if "code" in text:
            agent = "Coding Agent"

        elif "browser" in text:
            agent = "Browser Agent"

        elif "research" in text:
            agent = "Research Agent"

        else:
            agent = "Master Agent"

        return {
            "agent": agent,
            "reply": f"{agent} selected."
        }


brain = Brain()