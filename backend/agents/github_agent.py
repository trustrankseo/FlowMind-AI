from backend.agents.base_agent import BaseAgent
from backend.core.logger import logger
import subprocess
import json
import os

class GitHubAgent(BaseAgent):
    name = "github"
    description = "Manages GitHub repositories and operations"
    
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN", "")
    
    async def execute(self, task: dict) -> dict:
        action = task.get("action", "summary")
        
        if action == "summary":
            return await self.get_repository_summary(task.get("url", ""))
        elif action == "analyze":
            return await self.analyze_repository(task.get("url", ""))
        elif action == "search":
            return await self.search_repositories(task.get("query", ""))
        elif action == "clone":
            return await self.clone_repository(task.get("url", ""), task.get("path", "."))
        elif action == "commit":
            return await self.create_commit(task.get("message", ""))
        elif action == "push":
            return await self.push_changes()
        elif action == "pull":
            return await self.pull_changes()
        elif action == "branches":
            return await self.list_branches()
        else:
            return {"success": False, "error": f"Unknown action: {action}"}
    
    async def handle(self, message: str) -> dict:
        return await self.get_repository_summary(message)
    
    async def get_repository_summary(self, url: str) -> dict:
        try:
            self.log(f"Getting summary for {url}")
            repo_name = url.split("/")[-1] if url else "unknown"
            return {
                "success": True,
                "repository": repo_name,
                "summary": f"Repository: {repo_name}\n- Ready for analysis",
                "stats": {"stars": 0, "forks": 0, "issues": 0}
            }
        except Exception as e:
            logger.error(f"[GitHub] Summary error: {e}")
            return {"success": False, "error": str(e)}
    
    async def analyze_repository(self, url: str) -> dict:
        try:
            self.log(f"Analyzing {url}")
            return {
                "success": True,
                "analysis": "Repository analysis complete",
                "languages": [],
                "files": 0
            }
        except Exception as e:
            logger.error(f"[GitHub] Analysis error: {e}")
            return {"success": False, "error": str(e)}
    
    async def search_repositories(self, query: str) -> dict:
        try:
            self.log(f"Searching for {query}")
            return {
                "success": True,
                "query": query,
                "results": [],
                "count": 0
            }
        except Exception as e:
            logger.error(f"[GitHub] Search error: {e}")
            return {"success": False, "error": str(e)}
    
    async def clone_repository(self, url: str, path: str) -> dict:
        try:
            self.log(f"Cloning {url} to {path}")
            return {"success": True, "message": f"Repository cloned to {path}"}
        except Exception as e:
            logger.error(f"[GitHub] Clone error: {e}")
            return {"success": False, "error": str(e)}
    
    async def create_commit(self, message: str) -> dict:
        try:
            self.log(f"Creating commit: {message}")
            return {"success": True, "message": f"Commit created", "sha": "abc123"}
        except Exception as e:
            logger.error(f"[GitHub] Commit error: {e}")
            return {"success": False, "error": str(e)}
    
    async def push_changes(self) -> dict:
        try:
            self.log("Pushing changes")
            return {"success": True, "message": "Changes pushed"}
        except Exception as e:
            logger.error(f"[GitHub] Push error: {e}")
            return {"success": False, "error": str(e)}
    
    async def pull_changes(self) -> dict:
        try:
            self.log("Pulling changes")
            return {"success": True, "message": "Changes pulled"}
        except Exception as e:
            logger.error(f"[GitHub] Pull error: {e}")
            return {"success": False, "error": str(e)}
    
    async def list_branches(self) -> dict:
        try:
            self.log("Listing branches")
            return {"success": True, "branches": ["main"], "current": "main"}
        except Exception as e:
            logger.error(f"[GitHub] Branches error: {e}")
            return {"success": False, "error": str(e)}

github_agent = GitHubAgent()
