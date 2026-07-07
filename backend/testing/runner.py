import asyncio
import os


class TestRunner:
    """
    Runs pytest as a real subprocess and returns structured results.
    Restricted to running inside the project directory only — a chat
    message should never be able to make this run tests (or anything
    else) somewhere outside the project on disk.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = os.path.abspath(project_root)

    async def run(self, target: str = ".", timeout: int = 60):

        target_path = os.path.abspath(
            os.path.join(self.project_root, target)
        )

        if not target_path.startswith(self.project_root):
            return {
                "success": False,
                "error": "Target path is outside the project directory."
            }

        if not os.path.exists(target_path):
            return {
                "success": False,
                "error": f"Path not found: {target}"
            }

        process = await asyncio.create_subprocess_exec(
            "python", "-m", "pytest",
            target_path,
            "-v",
            "--tb=short",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=self.project_root
        )

        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )

        except asyncio.TimeoutError:
            process.kill()
            return {
                "success": False,
                "error": f"Test run timed out after {timeout}s."
            }

        output = stdout.decode() + stderr.decode()

        return {
            "success": process.returncode == 0,
            "return_code": process.returncode,
            "summary": self._extract_summary(output),
            "output": output
        }

    def _extract_summary(self, output: str) -> str:

        lines = output.strip().splitlines()

        for line in reversed(lines):

            lowered = line.lower()

            if "passed" in lowered or "failed" in lowered or "error" in lowered:
                return line.strip()

        return "No summary line found (no tests may have been collected)."


test_runner = TestRunner()
