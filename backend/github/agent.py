from backend.interfaces.base_agent import BaseAgent
from backend.github.service import github_service


class GitHubAgent(BaseAgent):

    name = "github"

    async def handle(self, message):

        root = "."

        if isinstance(message, dict):
            root = message.get("root", ".")

        return await github_service.summarize(root)


github_agent = GitHubAgent()