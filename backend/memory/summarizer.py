class MemorySummarizer:

    def summarize(self, messages):

        if not messages:
            return "No previous memory."

        return f"Conversation contains {len(messages)} messages."


memory_summarizer = MemorySummarizer()