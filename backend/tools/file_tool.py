from backend.tools.base import BaseTool


class FileTool(BaseTool):

    name = "file"

    description = "Read local files"

    async def execute(self, path=None):

        if not path:

            return "Path missing."

        try:

            with open(path, "r", encoding="utf-8") as f:

                return f.read()

        except Exception as e:

            return str(e)