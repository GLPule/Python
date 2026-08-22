# 🔢 Number Guessing Game

A command line number guessing game where the computer generates a random number within a user defined range and the player attempts to guess it.

##  Description

The player chooses a minimum and maximum number. The program then generates a random number within that range.

The player has a maximum of **7 attempts** to guess the correct number. After every incorrect guess, the program provides feedback indicating whether the guess was too high or too low.

The program also keeps track of the player's attempts and records the best score.

##  Features

* User defined number range
* Random number generation
* Maximum of 7 attempts per game
* High/low hints
* Attempt tracking
* Best score tracking
* Input validation
* Option to exit the game

##  Technologies

* Python 
* `random` module

##  Skills Demonstrated

* Variables
* Functions and program structure
* `while` loops
* Conditional statements
* Lists
* Random number generation
* User input
* Exception handling
* Score tracking
* Problem solving

##  How to Run

Run the program using Python:

```bash
python number_guessing_game.py
```

##  Example

```text
Do you want to start the game: yes
Enter the minimum number: 1
Enter the maximum number: 50

You have 7 attempts to guess the correct number
Guess the number (between 1-included and 50-included): 25
    Too high! Try again.

You have 6 attempts to guess the correct number
Guess the number (between 1-included and 50-included): 12
    Too low! Try again.

Congratulations! You guessed the number with 5 attempts.
Best Score: 5/7
Enter 'quiet' to end the game. Do you want to start the game: quiet
```

##  Possible Improvements

* Allow the player to select the number of attempts
* Add a scoring system based on difficulty (attempts)
* Add a leaderboard
* Prevent invalid minimum and maximum ranges
