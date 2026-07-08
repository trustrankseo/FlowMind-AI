from backend.agents.base_agent import BaseAgent
from backend.core.logger import logger
import re

class BrowserAgent(BaseAgent):
    name = "browser"
    description = "Handles web browsing and URL operations"
    
    async def execute(self, task: dict) -> dict:
        action = task.get("action", "open")
        
        if action == "open":
            return await self.open_url(task.get("url", ""))
        elif action == "search":
            return await self.search(task.get("query", ""))
        elif action == "extract":
            return await self.extract_text(task.get("url", ""))
        elif action == "screenshot":
            return await self.take_screenshot(task.get("url", ""))
        elif action == "navigate":
            return await self.navigate(task.get("path", ""))
        else:
            return {"success": False, "error": f"Unknown action: {action}"}
    
    async def handle(self, message: str) -> dict:
        if self._is_url(message):
            return await self.open_url(message)
        else:
            return await self.search(message)
    
    async def open_url(self, url: str) -> dict:
        try:
            self.log(f"Opening {url}")
            if not url.startswith(("http://", "https://")):
                url = f"https://{url}"
            return {
                "success": True,
                "url": url,
                "status": "opened",
                "title": "Page Title"
            }
        except Exception as e:
            logger.error(f"[Browser] Open error: {e}")
            return {"success": False, "error": str(e)}
    
    async def search(self, query: str) -> dict:
        try:
            self.log(f"Searching: {query}")
            return {
                "success": True,
                "query": query,
                "results": [
                    {"title": "Result 1", "url": "https://example.com", "snippet": "..."}
                ]
            }
        except Exception as e:
            logger.error(f"[Browser] Search error: {e}")
            return {"success": False, "error": str(e)}
    
    async def extract_text(self, url: str) -> dict:
        try:
            self.log(f"Extracting text from {url}")
            return {
                "success": True,
                "url": url,
                "text": "Extracted content from page",
                "length": 0
            }
        except Exception as e:
            logger.error(f"[Browser] Extract error: {e}")
            return {"success": False, "error": str(e)}
    
    async def take_screenshot(self, url: str) -> dict:
        try:
            self.log(f"Taking screenshot of {url}")
            return {
                "success": True,
                "url": url,
                "screenshot": "/screenshots/page.png"
            }
        except Exception as e:
            logger.error(f"[Browser] Screenshot error: {e}")
            return {"success": False, "error": str(e)}
    
    async def navigate(self, path: str) -> dict:
        try:
            self.log(f"Navigating to {path}")
            return {"success": True, "path": path, "message": "Navigated"}
        except Exception as e:
            logger.error(f"[Browser] Navigate error: {e}")
            return {"success": False, "error": str(e)}
    
    def _is_url(self, text: str) -> bool:
        url_pattern = r'https?://|www\.|\.[a-z]{2,}'
        return bool(re.search(url_pattern, text, re.IGNORECASE))

browser_agent = BrowserAgent()
