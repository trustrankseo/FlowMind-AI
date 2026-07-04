from backend.models.chat import ChatResponse
from backend.utils.memory import memory


class ChatService:

    def process(self, session_id: str, message: str):

        memory.add_message(session_id, "user", message)

        response = f"I received your message: {message}"

        memory.add_message(session_id, "assistant", response)

        return ChatResponse(
            success=True,
            response=response
        )


chat_service = ChatService()