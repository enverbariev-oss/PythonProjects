from venv import create

def count(text: str) -> dict[str, int]:
    words = text.lower().split()
    word_counts: dict[str, int] = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

word_counter: dict[str, int] = count("Hello World Hello")


