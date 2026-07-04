from backend.llm.prompts import SYSTEM_PROMPT


class ToolSelector:

    def build_prompt(
        self,
        user_message: str
    ):

        return f"""
{SYSTEM_PROMPT}

User:

{user_message}
"""


tool_selector = ToolSelector()