from backend.github.summary import repository_summary
from backend.providers.provider_manager import provider_manager


class GitHubService:

    async def summarize(self, root: str):

        summary = repository_summary.generate(root)

        provider = provider_manager.get_provider()

        prompt = f"""
You are a Senior Software Architect.

Analyze this repository summary.

Repository Summary:

{summary}

Explain:

1. Project Structure
2. Strengths
3. Weaknesses
4. Suggested Improvements
"""

        reply = await provider.chat(prompt)

        return {
            "summary": summary,
            "analysis": reply
        }


github_service = GitHubService()