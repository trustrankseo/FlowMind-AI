from backend.interfaces.base_tool import BaseTool
from backend.github.service import github_service


class GitHubTool(BaseTool):

    name = "github"

    async def execute(self, request):

        root = request.get("root", ".")

        return await github_service.summarize(
            root
        )


github_tool = GitHubTool()