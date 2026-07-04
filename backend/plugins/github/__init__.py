from backend.plugins.base import BasePlugin


class GitHubPlugin(BasePlugin):

    name = "github"

    version = "1.0.0"

    async def setup(self):
        return True


plugin = GitHubPlugin()