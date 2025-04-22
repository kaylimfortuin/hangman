# Hangman Game

A classic Hangman word guessing game implemented in Python. This console-based application provides a fun and interactive word-guessing experience with ASCII art visualization.

## Features

- Random word selection from a predefined dictionary
- ASCII art visualization of the Hangman's progress
- Interactive command-line interface
- Input validation and error handling
- Game state tracking (guessed letters, remaining attempts)
- Win/lose condition detection
- Option to play multiple rounds

## Installation

### Prerequisites
- Python 3.x

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/hangman.git
   cd hangman
   ```

2. No additional dependencies are required!

## Usage

Run the game using Python:

```bash
python main.py
```

Or make the script executable (Unix/Linux/Mac):

```bash
chmod +x main.py
./main.py
```

## How to Play

1. The computer will randomly select a word for you to guess.
2. For each round, you can guess one letter by typing it and pressing Enter.
3. If your guess is correct, the letter will be revealed in the word.
4. If your guess is incorrect, a piece of the hangman will be drawn.
5. You win if you guess the word before the hangman is complete.
6. You lose if the hangman is complete before you guess the word.

## Project Structure

- `main.py`: Main game loop and user interface
- `game.py`: Game mechanics and state management
- `words.py`: Word dictionary and random word selection

## License

This project is open source and available under the [MIT License](LICENSE).

