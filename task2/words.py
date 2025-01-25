import random;

WORDS_WITH_HINTS = {
    "python": "A popular programming language.",
    "hangman": "A classic word-guessing game.",
    "developer": "A person who writes code.",
    "computer": "An electronic device for processing data.",
    "software": "A collection of instructions that tell a computer what to do.",
    "keyboard": "A common input device.",
    "monitor": "An output device to display images.",
    "hardware": "Physical components of a computer system.",
    "database": "A structured set of data held in a computer.",
    "internet": "A global network connecting millions of computers.",
}

def get_random_word():
    word, hint = random.choice(list(WORDS_WITH_HINTS.items()))
    return word, hint
