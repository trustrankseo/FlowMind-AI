from backend.core.logger import logger
import os

class FileTool:
    name = "file"
    
    async def execute(self, request: dict) -> dict:
        try:
            action = request.get("action", "read")
            path = request.get("path", ".")
            
            if action == "read":
                return await self.read_file(path)
            elif action == "write":
                return await self.write_file(path, request.get("content", ""))
            elif action == "list":
                return await self.list_directory(path)
            elif action == "exists":
                return await self.check_exists(path)
            else:
                return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            logger.error(f"[FileTool] Error: {e}")
            return {"success": False, "error": str(e)}
    
    async def read_file(self, path: str) -> dict:
        try:
            if not os.path.exists(path):
                return {"success": False, "error": f"File not found: {path}"}
            with open(path, 'r') as f:
                content = f.read()
            return {
                "success": True,
                "path": path,
                "content": content,
                "size": len(content)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def write_file(self, path: str, content: str) -> dict:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            return {"success": True, "path": path, "message": "File written"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def list_directory(self, path: str) -> dict:
        try:
            if not os.path.exists(path):
                return {"success": False, "error": f"Directory not found: {path}"}
            items = os.listdir(path)
            return {"success": True, "path": path, "items": items}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def check_exists(self, path: str) -> dict:
        return {"success": True, "path": path, "exists": os.path.exists(path)}

file_tool = FileTool()
