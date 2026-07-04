from backend.providers.provider_manager import provider_manager


class CodeGenerator:

    async def generate(
        self,
        prompt: str
    ):

        provider = provider_manager.get_provider()

        return await provider.chat(
            f"""
You are an expert software engineer.

Generate production-ready code.

Task:

{prompt}
"""
        )


generator = CodeGenerator()