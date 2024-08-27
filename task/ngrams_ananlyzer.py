import re
from collections import Counter


def format_sentence(sentence: str):
    return re.sub(r'[^\w\s]', '', sentence).lower()


def generate_ngrams(sentences: tuple[str, ...], n=2):
    for sentence in sentences:
        words = tuple(format_sentence(sentence).split())
        for i in range(len(words) - n + 1):
            yield words[i:i + n]


def filter_common_ngrams(ngrams: list[tuple[str, ...]], limit=5):
    return Counter(ngrams).most_common(limit)


def find_ngrams(*sentences, n=2):
    return [ng for ng in generate_ngrams(sentences, n)]


def find_common_ngrams(*sentences, n=2, limit=5):
    ngrams = find_ngrams(*sentences, n=n)
    most_common = Counter(ngrams).most_common(limit)
    return list([item for item, _ in most_common])
