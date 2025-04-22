#!/usr/bin/env python3
"""
Main module for the Hangman game.

This module serves as the entry point for the Hangman game, handling user
interaction and game flow.
"""

import os
import platform
import time
from typing import List, NoReturn

from game import HangmanGame
from words import get_random_word


def clear_screen() -> None:
    """
    Clear the console screen based on the operating system.
    """
    # Check the operating system and use the appropriate command
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_title() -> None:
    """
    Print the game title banner.
    """
    title = """
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """
    print(title)
    print("\n" + "=" * 70 + "\n")


def print_instructions() -> None:
    """
    Print the game instructions.
    """
    instructions = """
    INSTRUCTIONS:
    
    1. The computer will randomly select a word for you to guess.
    2. Each round, you can guess one letter.
    3. If your guess is correct, the letter will be revealed in the word.
    4. If your guess is incorrect, a piece of the hangman will be drawn.
    5. You win if you guess the word before the hangman is complete.
    6. You lose if the hangman is complete before you guess the word.
    
    Good luck!
    """
    print(instructions)
    print("=" * 70 + "\n")


def display_game_state(game: HangmanGame, guessed_letters: List[str]) -> None:
    """
    Display the current state of the game.
    
    Args:
        game (HangmanGame): The current game instance.
        guessed_letters (List[str]): A list of letters that have been guessed.
    """
    # Display the hangman
    print(game.display_hangman())
    
    # Display the word (with underscores for unguessed letters)
    print(f"\nWord: {game.display_word()}\n")
    
    # Display guessed letters
    if guessed_letters:
        print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")
    
    # Display correct and incorrect guesses
    correct_guesses = game.get_correct_guesses()
    if correct_guesses:
        print(f"Correct guesses: {', '.join(sorted(correct_guesses))}")
    
    incorrect_guesses = game.get_incorrect_guesses()
    if incorrect_guesses:
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")
    
    # Display remaining attempts
    print(f"\nRemaining attempts: {game.remaining_attempts}")
    print("\n" + "-" * 70 + "\n")


def get_valid_guess(guessed_letters: List[str]) -> str:
    """
    Get a valid guess from the user.
    
    A valid guess is a single alphabetic character that hasn't been guessed before.
    
    Args:
        guessed_letters (List[str]): A list of letters that have been guessed.
        
    Returns:
        str: A valid letter guess.
    """
    while True:
        guess = input("Enter your guess (a single letter): ").strip().lower()
        
        # Check if input is a single character
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        # Check if input is alphabetic
        if not guess.isalpha():
            print("Please enter a letter from A-Z.")
            continue
        
        # Check if letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        return guess


def play_game() -> bool:
    """
    Play a single game of Hangman.
    
    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    # Select a random word
    word = get_random_word()
    
    # Create a new game
    game = HangmanGame(word)
    
    # Keep track of guessed letters
    guessed_letters = []
    
    # Main game loop
    while not game.is_game_over():
        clear_screen()
        print_title()
        
        # Display current game state
        display_game_state(game, guessed_letters)
        
        try:
            # Get a valid guess from the user
            guess = get_valid_guess(guessed_letters)
            
            # Make the guess
            valid_guess = game.guess_letter(guess)
            
            if valid_guess:
                # Add the guess to the list of guessed letters
                guessed_letters.append(guess)
                
                # Give feedback on the guess
                if guess in word:
                    print(f"Good guess! '{guess}' is in the word.")
                else:
                    print(f"Sorry, '{guess}' is not in the word.")
            
            # Brief pause for readability
            time.sleep(1)
            
        except ValueError as e:
            print(f"Error: {e}")
            time.sleep(2)
    
    # Game over - display final state
    clear_screen()
    print_title()
    display_game_state(game, guessed_letters)
    
    # Display game result
    if game.get_game_result():
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")
    
    # Ask if the player wants to play again
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again in ['y', 'yes']:
            return True
        elif play_again in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def main() -> NoReturn:
    """
    Main function to start the game.
    """
    try:
        # Welcome message
        clear_screen()
        print_title()
        print_instructions()
        
        input("Press Enter to start the game...")
        
        # Main game loop
        while True:
            if not play_game():
                break
        
        # Thank the player
        clear_screen()
        print_title()
        print("Thank you for playing Hangman! Goodbye!")
        
    except KeyboardInterrupt:
        # Handle Ctrl+C to exit gracefully
        clear_screen()
        print("\nGame interrupted. Goodbye!")
    except Exception as e:
        # Handle unexpected errors
        print(f"\nAn unexpected error occurred: {e}")
    
    # Exit the program
    exit(0)


if __name__ == "__main__":
    main()

