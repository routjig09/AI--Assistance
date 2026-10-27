
from typing import ClassVar

import pytest

from app.models import Conversation, Message, Role, User


def test_user_gets_unique_id():
    user1 = User(name="Jiggy")
    user2 = User(name="Alex")

    assert user1.user_id != user2.user_id


def test_conversation_stores_messages():
    user = User(name="Jiggy")
    conversation = Conversation(user=user)

    message = Message(role=Role.USER, content="Hello AI")
    conversation.add_message(message)

    assert len(conversation.get_history()) == 1
    assert conversation.get_history()[0].content == "Hello AI"


def test_conversation_message_count():
    conversation = Conversation(user=User(name="Jiggy"))
    conversation.add_message(Message(role=Role.USER, content="Hello AI"))
    conversation.add_message(Message(role=Role.ASSISTANT, content="Hello"))

    assert conversation.message_count() == 2


def test_conversation_returns_only_user_messages():
    conversation = Conversation(user=User(name="Jiggy"))
    user_message = Message(role=Role.USER, content="Hello AI")
    conversation.add_message(user_message)
    conversation.add_message(Message(role=Role.ASSISTANT, content="Hello"))
    conversation.add_message(Message(role=Role.SYSTEM, content="Be helpful"))

    assert conversation.get_user_messages() == [user_message]


def test_conversation_rejects_more_than_100_messages():
    conversation = Conversation(user=User(name="Jiggy"))

    for index in range(100):
        conversation.add_message(
            Message(role=Role.USER, content=f"Message {index}")
        )

    assert conversation.message_count() == 100
    with pytest.raises(ValueError, match="cannot contain more than 100 messages"):
        conversation.add_message(Message(role=Role.USER, content="One too many"))


def test_empty_message_is_rejected():
    with pytest.raises(ValueError):
        Message(role=Role.USER, content="   ")


def test_conversations_have_independent_message_lists():
    user = User(name="Jiggy")
    first = Conversation(user=user)
    second = Conversation(user=user)

    first.add_message(Message(role=Role.USER, content="Hello"))

    assert len(first.messages) == 1
    assert len(second.messages) == 0
    
