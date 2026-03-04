# 🎯 Number Guessing Game

A simple command-line number guessing game written in Python.

## How to Play

1. Run the script — the program picks a random number between **1 and 100**
2. You have **7 attempts** to guess it
3. After each guess you'll get a hint: *Too High* or *Too Low*
4. Guess correctly before running out of attempts to win!

## Requirements

- Python 3.x (no external libraries needed)

## Running the Game

```bash
python guessing_game.py
```

## Example

```
---Welcome to the Number Guessing Game Challenge!---
I'm thinking of a number between 1 and 100. You have 7 chances.

Attempt 1: Enter Your Guess Please: 50
Too High! Please Try A Lower Number.
Remaining attempts: 6

Attempt 2: Enter Your Guess Please: 25
Too Low! Please Try A Higher Number.
Remaining attempts: 5

Attempt 3: Enter Your Guess Please: 37
🪶 Congratulations! 🪶 You guessed it in 3 attempts.
```

## Project Structure

```
📁 number-guessing-game
└── guessing_game.py   # Main game script
└── README.md          # Project documentation
```
