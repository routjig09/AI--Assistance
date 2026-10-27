
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar
from uuid import uuid4


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@dataclass
class User:
    name: str
    user_id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Message:
    role: Role
    content: str
    message_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise ValueError("Message content cannot be empty")


@dataclass
class Conversation:
    MAX_MESSAGES: ClassVar[int] = 100

    user: User
    conversation_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    messages: list[Message] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.messages) > self.MAX_MESSAGES:
            raise ValueError(
                f"A conversation cannot contain more than {self.MAX_MESSAGES} messages"
            )

    def add_message(self, message: Message) -> None:
        if len(self.messages) >= self.MAX_MESSAGES:
            raise ValueError(
                f"A conversation cannot contain more than {self.MAX_MESSAGES} messages"
            )
        self.messages.append(message)

    def get_history(self) -> list[Message]:
        return list(self.messages)

    def message_count(self) -> int:
        return len(self.messages)

    def get_user_messages(self) -> list[Message]:
        return [message for message in self.messages if message.role == Role.USER]
    
    
    def message_count(self)-> int :
        return len(self.messages)
    
    def get_user_messages(self) -> list[Message]:
        return[Message for message in self.messages if message.role == Role.USER]
    MAX_MESSAGES: ClassVar[int] = 100

def add_message(self, message):
    if len(self.messages) >= self.MAX_MESSAGES:
        raise ValueError(...)
    self.messages.append(message)
    
    

    
    


    