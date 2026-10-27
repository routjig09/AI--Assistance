
from app.processor import (
    chunk_text,
    count_words,
    normalize_message,
    word_frequency,
)


def main() -> None:
    text = "  Python   makes AI development practical  "

    print("Normalized:", normalize_message(text))
    print("Word count:", count_words(text))
    print("Word frequency:", word_frequency(text))
    print("Chunks:", list(chunk_text(text, chunk_size=3)))


if __name__ == "__main__":
    main()
