# ⛰📄✂️ Rock Paper Scissors

A command line Rock Paper Scissors game implemented in Python with support for both **single-player** and **two-player** gameplay.

##  Description

The game allows Player 1 to compete against either the computer or another player.

Each game consists of multiple rounds and the first player to win **3 rounds** wins the overall game.

The program also displays the current score and number of tied rounds.

##  Features

* Play against the computer
* Play against another player
* Best-of-five style gameplay
* Score tracking
* Tie tracking
* Random computer choices
* Emoji-based choice display
* Input-based game control
* Option to quit

##  Game Rules

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
```

If both players choose the same option, the round is a tie.

##  Technologies

* Python 
* `random` module

##  Skills Demonstrated

* Functions
* Dictionaries
* Variables and constants
* Conditional statements
* `while` loops
* User input
* Random selection
* Game logic
* Score tracking
* String formatting

##  How to Run

Run the program:

```bash
python rock_paper_scissor.py
```

Choose a game mode:

```text
Play against (Computer/Player/Quit): computer
```

Then enter:

```text
P1: Rock, paper or scissors? (r/p/s): r
```

The program displays the choices and the result of each round.

##  Example

```text
Play against (Computer/Player/Quit): computer

P1: Rock, paper or scissors? (r/p/s): r
Player 1 ⛰️
Computer: ✂️

Player 1 wins Round 1
Score: 1 - 0 | Ties: 0
```

##  Possible Improvements

* Add a graphical user interface
* Add difficulty levels
* Allow the player to select the number of rounds
* Save game statistics
* Add sound effects
* Add a leaderboard
* Improve input validation
