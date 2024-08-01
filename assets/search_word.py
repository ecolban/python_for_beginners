from collections import Counter
from collections.abc import Iterable
from functools import partial
from math import log

with open('wordle-La.txt') as f:
    WORDS_LA: list[str] = [w.strip() for w in f]


def find_words(guesses: Iterable[tuple[str, str]]) -> list[str]:
    words = [word for word in WORDS_LA if all(feedback(guess, word) == fb for guess, fb in guesses)]
    return words


def feedback(guess: str, word: str) -> str:
    matched = {i: i for i, (c1, c2) in enumerate(zip(guess, word)) if c1 == c2}
    for i, c1 in enumerate(guess):
        j = next((j for j, c2 in enumerate(word) if c1 == c2 and j not in matched.values()), None)
        if j is not None:
            matched[i] = j
    return ''.join(c1.upper() if word[i] == c1 else c1 if i in matched else '_' for i, c1 in enumerate(guess))


def info(guess: str, words: list[str]) -> float:
    n = len(words)
    c = Counter(feedback(guess, word) for word in words)
    return sum(-(p := v / n) * log(p) for v in c.values())


if __name__ == '__main__':
    words = find_words([
        ('raise', 'r__sE'),
        ('perch', '_er_h'),
    ])
    print(words)
    best = sorted(((info(guess, words), guess) for guess in WORDS_LA), reverse=True)
    print(best[:10])

