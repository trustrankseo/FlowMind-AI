from backend.models.chat import ChatResponse


class ChatService:

    def process(self, message: str):

        return ChatResponse(
            success=True,
            response=f"You said: {message}"
        )


chat_service = ChatService()