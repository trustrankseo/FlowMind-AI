from backend.interfaces.base_tool import BaseTool
from backend.deployment.deployer import deployer


class DeploymentTool(BaseTool):

    name = "deployment"

    async def execute(self, request):

        return await deployer.deploy()


deployment_tool = DeploymentTool()
