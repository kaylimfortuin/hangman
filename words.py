#!/usr/bin/env python3
"""
Words module for the Hangman game.

This module contains a list of words that can be used in the Hangman game,
as well as a function to randomly select a word from the list.
"""

import random

# List of words for the Hangman game
# All words are lowercase, contain no special characters or numbers,
# and vary in length from 4 to 10 characters
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
    """
    Select and return a random word from the word list.
    
    Returns:
        str: A randomly selected word from WORD_LIST.
    """
    return random.choice(WORD_LIST)


if __name__ == "__main__":
    # Test the function if this module is run directly
    print(f"Random word: {get_random_word()}")

