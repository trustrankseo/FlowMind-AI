import asyncio

from backend.core.logger import logger


class Deployer:
    """
    Runs a fixed, whitelisted deployment sequence — never arbitrary
    shell commands from user/chat input. This keeps a chat message from
    ever being able to run something unintended on the server.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = project_root

    async def deploy(self):

        steps = [
            ("git_pull", ["git", "pull"]),
            ("install_dependencies", ["pip", "install", "-r", "requirements.txt", "--break-system-packages"]),
        ]

        results = []

        for step_name, command in steps:

            result = await self._run(command)
            result["step"] = step_name
            results.append(result)

            if not result["success"]:
                # Stop the sequence if a step fails, rather than
                # continuing to install/deploy on top of a bad pull.
                break

        return {
            "success": all(r["success"] for r in results),
            "steps": results
        }

    async def _run(self, command: list, timeout: int = 120):

        try:

            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.project_root
            )

            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )

            output = stdout.decode() + stderr.decode()

            return {
                "success": process.returncode == 0,
                "command": " ".join(command),
                "output": output
            }

        except asyncio.TimeoutError:

            process.kill()

            return {
                "success": False,
                "command": " ".join(command),
                "output": f"Timed out after {timeout}s."
            }

        except Exception as error:

            logger.error(f"[Deployer] step failed: {error}")

            return {
                "success": False,
                "command": " ".join(command),
                "output": str(error)
            }


deployer = Deployer()
