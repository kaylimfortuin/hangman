from typing import Set, List, Optional


class HangmanGame:
    # ASCII art for Hangman states (from 0 incorrect attempts to 6)
    HANGMAN_STATES = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]
    
    def __init__(self, word: str, max_attempts: int = 6):
        """
        Initialize a new game of Hangman.
        
        Args:
            word (str): The word to be guessed.
            max_attempts (int, optional): The maximum number of incorrect guesses allowed. Defaults to 6.
        
        Raises:
            ValueError: If the word is empty or contains non-alphabetic characters.
        """
        # Validate the word
        if not word:
            raise ValueError("Word cannot be empty")
        if not word.isalpha():
            raise ValueError("Word must contain only alphabetic characters")
        
        self.word = word.lower()
        self.guessed_letters: Set[str] = set()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
    
    def display_word(self) -> str:
        """
        Get the current display of the word with underscores for unguessed letters.
        
        Returns:
            str: The word with guessed letters revealed and unguessed letters as underscores.
        """
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)
    
    def display_hangman(self) -> str:
        """
        Get the ASCII art representation of the current hangman state.
        
        Returns:
            str: ASCII art of the hangman.
        """
        # Calculate the state index based on incorrect guesses
        state_index = self.max_attempts - self.remaining_attempts
        return self.HANGMAN_STATES[state_index]
    
    def guess_letter(self, letter: str) -> bool:
        """
        Make a guess with a letter.
        
        Args:
            letter (str): The letter being guessed.
            
        Returns:
            bool: True if the guess was valid and processed, False otherwise.
            
        Raises:
            ValueError: If the input is not a single alphabetic character.
        """
        # Validate the guess
        if not letter or len(letter) != 1:
            raise ValueError("Guess must be a single character")
        
        letter = letter.lower()
        
        if not letter.isalpha():
            raise ValueError("Guess must be an alphabetic character")
        
        if letter in self.guessed_letters:
            return False  # Letter was already guessed
        
        # Add the letter to guessed letters
        self.guessed_letters.add(letter)
        
        # If the letter is not in the word, decrement remaining attempts
        if letter not in self.word:
            self.remaining_attempts -= 1
        
        return True
    
    def is_word_guessed(self) -> bool:
        """
        Check if the word has been completely guessed.
        
        Returns:
            bool: True if all letters in the word have been guessed, False otherwise.
        """
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_game_over(self) -> bool:
        """
        Check if the game is over (either won or lost).
        
        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.is_word_guessed() or self.remaining_attempts <= 0
    
    def get_game_result(self) -> Optional[bool]:
        """
        Get the result of the game.
        
        Returns:
            Optional[bool]: True if the player won, False if the player lost, None if the game is still in progress.
        """
        if not self.is_game_over():
            return None
        
        return self.is_word_guessed()
    
    def get_incorrect_guesses(self) -> List[str]:
        """
        Get a list of incorrect guesses.
        
        Returns:
            List[str]: A list of letters that were guessed but are not in the word.
        """
        return [letter for letter in self.guessed_letters if letter not in self.word]
    
    def get_correct_guesses(self) -> List[str]:
        """
        Get a list of correct guesses.
        
        Returns:
            List[str]: A list of letters that were guessed and are in the word.
        """
        return [letter for letter in self.guessed_letters if letter in self.word]

