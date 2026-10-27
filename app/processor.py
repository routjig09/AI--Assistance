
from collections import Counter


def normalize_message(message: str) -> str:
    """Remove unnecessary whitespace from a message."""
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    normalized = " ".join(message.split())

    if not normalized:
        raise ValueError("message cannot be empty")

    return normalized


def count_words(message: str) -> int:
    """Count whitespace-separated words."""
    return len(normalize_message(message).split())


def word_frequency(message: str) -> dict[str, int]:
    """Count word occurrences without case sensitivity."""
    words = normalize_message(message).lower().split()
    return dict(Counter(words))


def chunk_text(message: str, chunk_size: int = 5):
    """Yield consecutive word chunks of a specified maximum size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    words = normalize_message(message).split()

    for start in range(0, len(words), chunk_size):
        yield " ".join(words[start:start + chunk_size])
