#!/usr/bin/env python3
import random
WORD_LIST = [
    "python",
    "hangman",
    "computer",
    "programming",
    "keyboard",
    "developer",
    "algorithm",
    "function",
    "variable",
    "language",
    "code",
    "game",
    "player",
    "screen",
    "console",
    "challenge",
    "guess",
    "letter",
    "word",
    "puzzle",
    "logic",
    "software",
    "interface",
    "network",
    "database",
]


def get_random_word():
    return random.choice(WORD_LIST)
