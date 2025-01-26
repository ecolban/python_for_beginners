from collections import Counter
from collections.abc import Iterable
from math import log
from wordlebot_solutions import SOLUTIONS

guesses = SOLUTIONS['normal-simple']['guesses']
WORDS = guesses.keys()

with open('wordle-Ta.txt') as f:
    WORDS_ALLOWED: set[str] = WORDS | {w.strip() for w in f}

def find_words(guesses: Iterable[tuple[str, str]]) -> list[str]:
    return [word for word in WORDS if all(feedback(guess, word) == fb for guess, fb in guesses)]


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
    return sum((p := v / n) * -log(p, 2) for v in c.values())


if __name__ == '__main__':
    print(len(WORDS))
    print(len(WORDS_ALLOWED))
    words = find_words([
        ('raise', '__is_'),
        ('south', 'S_U__'),
    ])
    print(len(words), words)
    best_overall = sorted(((info(guess, words), guess) for guess in WORDS), reverse=True)
    best_possible_only = sorted(((info(guess, words), guess) for guess in words), reverse=True)
    print(f'{best_possible_only[:5]}')
    print(f'{best_overall[:5]}')
