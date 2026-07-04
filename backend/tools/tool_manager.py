from backend.tools.registry import registry

from backend.tools.file_tool import FileTool
from backend.tools.search_tool import SearchTool
from backend.tools.code_tool import CodeTool
from backend.tools.browser_tool import BrowserTool


registry.register(FileTool())
registry.register(SearchTool())
registry.register(CodeTool())
registry.register(BrowserTool())


class ToolManager:

    def get(self, name):

        return registry.get(name)

    def list(self):

        return registry.all()


tool_manager = ToolManager()