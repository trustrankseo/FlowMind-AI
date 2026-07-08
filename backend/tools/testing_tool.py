from backend.core.logger import logger
import subprocess
import json
import os

class TestingTool:
    name = "testing"
    
    async def execute(self, request: dict) -> dict:
        try:
            path = request.get("path", ".")
            logger.info(f"[TestingTool] Running tests in {path}")
            
            # Run pytest
            result = subprocess.run(
                ["pytest", path, "-v", "--tb=short"],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            return {
                "success": result.returncode == 0,
                "path": path,
                "output": result.stdout,
                "errors": result.stderr,
                "exit_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Test execution timed out"}
        except Exception as e:
            logger.error(f"[TestingTool] Error: {e}")
            return {"success": False, "error": str(e)}

testing_tool = TestingTool()
