
import pytest

from app.processor import (
    chunk_text,
    count_words,
    normalize_message,
    word_frequency,
)


def test_normalize_message():
    assert normalize_message("  Hello   AI  ") == "Hello AI"


def test_count_words():
    assert count_words("Hello AI assistant") == 3


def test_word_frequency():
    assert word_frequency("AI ai Python") == {
        "ai": 2,
        "python": 1,
    }


def test_chunk_text():
    assert list(chunk_text("one two three four", 2)) == [
        "one two",
        "three four",
    ]


def test_empty_message_is_rejected():
    with pytest.raises(ValueError):
        normalize_message("   ")


def test_invalid_chunk_size_is_rejected():
    with pytest.raises(ValueError):
        list(chunk_text("hello world", 0))
