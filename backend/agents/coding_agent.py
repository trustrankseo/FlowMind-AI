from backend.agents.base_agent import BaseAgent
from backend.core.logger import logger
import os
import json
from pathlib import Path

class CodingAgent(BaseAgent):
    name = "coding"
    description = "Handles code reading, writing, and analysis"
    
    def __init__(self):
        self.project_root = "."
    
    async def execute(self, task: dict) -> dict:
        action = task.get("action", "read")
        
        if action == "read":
            return await self.read_file(task.get("path", ""))
        elif action == "write":
            return await self.write_file(task.get("path", ""), task.get("content", ""))
        elif action == "replace":
            return await self.replace_text(task.get("path", ""), task.get("old", ""), task.get("new", ""))
        elif action == "create":
            return await self.create_file(task.get("path", ""), task.get("content", ""))
        elif action == "delete":
            return await self.delete_file(task.get("path", ""))
        elif action == "search":
            return await self.search_project(task.get("query", ""))
        elif action == "explain":
            return await self.explain_code(task.get("path", ""))
        elif action == "refactor":
            return await self.refactor_code(task.get("path", ""))
        else:
            return {"success": False, "error": f"Unknown action: {action}"}
    
    async def handle(self, message: str) -> dict:
        return await self.search_project(message)
    
    async def read_file(self, path: str) -> dict:
        try:
            self.log(f"Reading {path}")
            full_path = os.path.join(self.project_root, path)
            if not os.path.exists(full_path):
                return {"success": False, "error": f"File not found: {path}"}
            with open(full_path, 'r') as f:
                content = f.read()
            return {
                "success": True,
                "path": path,
                "content": content,
                "lines": len(content.split('\n'))
            }
        except Exception as e:
            logger.error(f"[Coding] Read error: {e}")
            return {"success": False, "error": str(e)}
    
    async def write_file(self, path: str, content: str) -> dict:
        try:
            self.log(f"Writing to {path}")
            full_path = os.path.join(self.project_root, path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                f.write(content)
            return {"success": True, "path": path, "message": "File written"}
        except Exception as e:
            logger.error(f"[Coding] Write error: {e}")
            return {"success": False, "error": str(e)}
    
    async def replace_text(self, path: str, old: str, new: str) -> dict:
        try:
            self.log(f"Replacing text in {path}")
            result = await self.read_file(path)
            if not result["success"]:
                return result
            content = result["content"]
            new_content = content.replace(old, new)
            return await self.write_file(path, new_content)
        except Exception as e:
            logger.error(f"[Coding] Replace error: {e}")
            return {"success": False, "error": str(e)}
    
    async def create_file(self, path: str, content: str) -> dict:
        try:
            self.log(f"Creating {path}")
            full_path = os.path.join(self.project_root, path)
            if os.path.exists(full_path):
                return {"success": False, "error": f"File already exists: {path}"}
            return await self.write_file(path, content)
        except Exception as e:
            logger.error(f"[Coding] Create error: {e}")
            return {"success": False, "error": str(e)}
    
    async def delete_file(self, path: str) -> dict:
        try:
            self.log(f"Deleting {path}")
            full_path = os.path.join(self.project_root, path)
            if not os.path.exists(full_path):
                return {"success": False, "error": f"File not found: {path}"}
            os.remove(full_path)
            return {"success": True, "path": path, "message": "File deleted"}
        except Exception as e:
            logger.error(f"[Coding] Delete error: {e}")
            return {"success": False, "error": str(e)}
    
    async def search_project(self, query: str) -> dict:
        try:
            self.log(f"Searching for {query}")
            results = []
            for root, dirs, files in os.walk(self.project_root):
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                for file in files:
                    if file.endswith(('.py', '.js', '.ts', '.jsx', '.tsx')):
                        filepath = os.path.join(root, file)
                        try:
                            with open(filepath, 'r') as f:
                                if query.lower() in f.read().lower():
                                    results.append(filepath)
                        except:
                            pass
            return {"success": True, "query": query, "results": results[:10]}
        except Exception as e:
            logger.error(f"[Coding] Search error: {e}")
            return {"success": False, "error": str(e)}
    
    async def explain_code(self, path: str) -> dict:
        try:
            self.log(f"Explaining {path}")
            result = await self.read_file(path)
            if not result["success"]:
                return result
            return {
                "success": True,
                "path": path,
                "explanation": "Code explanation would go here"
            }
        except Exception as e:
            logger.error(f"[Coding] Explain error: {e}")
            return {"success": False, "error": str(e)}
    
    async def refactor_code(self, path: str) -> dict:
        try:
            self.log(f"Refactoring {path}")
            return {
                "success": True,
                "path": path,
                "suggestions": "Refactoring suggestions would go here"
            }
        except Exception as e:
            logger.error(f"[Coding] Refactor error: {e}")
            return {"success": False, "error": str(e)}

coding_agent = CodingAgent()
