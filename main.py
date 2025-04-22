#!/usr/bin/env python3
import os
import platform
import time
from typing import List, NoReturn

from game import HangmanGame
from words import get_random_word


def clear_screen() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_title() -> None:
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
    print(game.display_hangman())
    
    print(f"\nWord: {game.display_word()}\n")
    
    if guessed_letters:
        print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")
    
    correct_guesses = game.get_correct_guesses()
    if correct_guesses:
        print(f"Correct guesses: {', '.join(sorted(correct_guesses))}")
    
    incorrect_guesses = game.get_incorrect_guesses()
    if incorrect_guesses:
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")
    
    print(f"\nRemaining attempts: {game.remaining_attempts}")
    print("\n" + "-" * 70 + "\n")


def get_valid_guess(guessed_letters: List[str]) -> str:
    while True:
        guess = input("Enter your guess (a single letter): ").strip().lower()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if not guess.isalpha():
            print("Please enter a letter from A-Z.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        return guess


def play_game() -> bool:
    word = get_random_word()
    
    game = HangmanGame(word)
    
    guessed_letters = []
    
    while not game.is_game_over():
        clear_screen()
        print_title()
        
        display_game_state(game, guessed_letters)
        
        try:
            guess = get_valid_guess(guessed_letters)
            
            valid_guess = game.guess_letter(guess)
            
            guessed_letters.append(guess)
            
            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word.")
            
            time.sleep(1)
            
        except ValueError as e:
            print(f"Error: {e}")
            time.sleep(2)
    
    clear_screen()
    print_title()
    display_game_state(game, guessed_letters)
    
    if game.get_game_result():
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")
    
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again in ['y', 'yes']:
            return True
        elif play_again in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def main() -> NoReturn:
    try:
        clear_screen()
        print_title()
        print_instructions()
        
        input("Press Enter to start the game...")
        
        while True:
            if not play_game():
                break
        
        clear_screen()
        print_title()
        print("Thank you for playing Hangman! Goodbye!")
        
    except KeyboardInterrupt:
        clear_screen()
        print("\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    exit(0)


if __name__ == "__main__":
    main()

