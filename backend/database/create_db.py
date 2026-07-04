from backend.database.base import Base
from backend.database.session import engine

# Import all models
from backend.database.models.conversation import Conversation
from backend.database.models.message import Message

Base.metadata.create_all(bind=engine)

print("✅ FlowMind Database Created Successfully")