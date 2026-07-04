from backend.providers.provider_manager import provider_manager
from backend.llm.tool_selector import tool_selector
from backend.llm.formatter import formatter


class LLMOrchestrator:

    async def select_tool(self, message: str):

        provider = provider_manager.get_provider()

        prompt = tool_selector.build_prompt(message)

        response = await provider.chat(prompt)

        decision = formatter.parse(response)

        return decision


orchestrator = LLMOrchestrator()