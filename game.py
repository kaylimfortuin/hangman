from typing import Set, List, Optional


class HangmanGame:
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
        if not word:
            raise ValueError("Word cannot be empty")
        if not word.isalpha():
            raise ValueError("Word must contain only alphabetic characters")
        
        self.word = word.lower()
        self.guessed_letters: Set[str] = set()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
    
    def display_word(self) -> str:
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)
    
    def display_hangman(self) -> str:
        state_index = self.max_attempts - self.remaining_attempts
        return self.HANGMAN_STATES[state_index]
    
    def guess_letter(self, letter: str) -> bool:
        if not letter or len(letter) != 1:
            raise ValueError("Guess must be a single character")
        
        letter = letter.lower()
        
        if not letter.isalpha():
            raise ValueError("Guess must be an alphabetic character")
        
        if letter in self.guessed_letters:
            return False  # Letter was already guessed
        
        # Add the letter to guessed letters
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.remaining_attempts -= 1
        
        return True
    
    def is_word_guessed(self) -> bool:
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_game_over(self) -> bool:
        return self.is_word_guessed() or self.remaining_attempts <= 0
    
    def get_game_result(self) -> Optional[bool]:
        if not self.is_game_over():
            return None
        
        return self.is_word_guessed()
    
    def get_incorrect_guesses(self) -> List[str]:
        return [letter for letter in self.guessed_letters if letter not in self.word]
    
    def get_correct_guesses(self) -> List[str]:
        return [letter for letter in self.guessed_letters if letter in self.word]

