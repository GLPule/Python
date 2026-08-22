# 🎲 Dice Rolling Game

A simple Python command line application that allows the user to choose how many dice they want to roll and generates random results for each die.

## Description

The program asks the user how many dice they want to roll, generates a random value between 1 and 6 for each die and displays the results.

The user can continue rolling the selected number of dice until they choose to exit.

## Features

- Choose the number of dice to roll
- Generate random dice values
- Roll the dice multiple times
- Track the number of rolls
- Validate user input
- Prevent rolling zero dice
- Handle invalid input

## Technologies

- Python
- `random` module

## Skills Demonstrated

- Functions
- `for` loops
- `while` loops
- Conditional statements
- Lists
- User input
- Error handling with `try` and `except`
- Random number generation

## How to Run

Make sure Python is installed on your computer.

Run the program:

```bash
python dice_rolling.py
```

## Example

```text
How many dice to you want to roll: 3

Roll the dice? (y/n): y
Rolling: 1
[4, 2, 6]

Roll the dice? (y/n): y
Rolling: 2
[1, 5, 3]

Roll the dice? (y/n): n
Thanks for playing the game.
```

## Possible Improvements

- Add different types of dice such as D4, D8, D10, D12, and D20
- Calculate and display the total of the dice
- Display graphical dice
- Add statistics such as highest, lowest, and average roll
- Add a graphical user interface (GUI)
