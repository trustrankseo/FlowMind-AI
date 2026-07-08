from backend.core.logger import logger
from typing import List, Dict

class MemorySummarizer:
    def summarize(self, messages: List[Dict[str, str]], max_length: int = 500) -> str:
        if not messages:
            return "No previous history."
        try:
            summary_parts = []
            for msg in messages[-5:]:
                role = msg.get("role", "unknown").capitalize()
                content = msg.get("content", "")[:100]
                summary_parts.append(f"{role}: {content}")
            summary = "\n".join(summary_parts)
            if len(summary) > max_length:
                summary = summary[:max_length] + "..."
            return summary
        except Exception as error:
            logger.error(f"[MemorySummarizer] Error: {error}")
            return "Error summarizing."

memory_summarizer = MemorySummarizer()
