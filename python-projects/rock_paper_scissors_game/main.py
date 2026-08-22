import random

ROCK = "r"
PAPER = "p"
SCISSOR = "s"
play = True
overall = 3

def decision(user, opponent):
    if user == opponent:
        return "Tie"
    elif (
        (user == ROCK and opponent == SCISSOR) or 
        (user == PAPER and opponent == ROCK) or
        (user == SCISSOR and opponent == PAPER)):
        return "You win"
    return "You lose"

choice = {
    "r" : "⛰️",
    "p": "📄",
    "s": "✂️"
}

while True:
    start = input("Play against (Computer/Player/Quit): ").strip().lower()
    if start == "quit":
        break

    player1_wins = 0
    player2_wins = 0
    ties = 0
    round = 0

    while player1_wins < overall and player2_wins < overall:
        user1 = input("P1: Rock, paper or scissors? (r/p/s): ")
        if start == "computer":
            user2 = random.choice([ROCK, PAPER, SCISSOR])
        else:
            user2 = input("P2: Rock, paper or scissors? (r/p/s): ")

        round += 1
        print(f"Player 1 {choice[user1]}")
        print(f"{"Computer" if start == "computer" else "Player 2"}: {choice[user2]}")

        results = decision(user1, user2)

        if results == "You win":
            player1_wins += 1
            print(f"Player 1 wins Round {round}")
        elif results == "You lose":
            player2_wins += 1
            print(f"{"Computer" if start == "computer" else "Player 2"} wins Round {round}")
        else:
            ties += 1
            print(f"Round {round} is a Tie")

        print(f"Score: {player1_wins} - {player2_wins} | Ties: {ties}")
    print(f"{"Player 1" if player1_wins == overall else ("Computer" if start == "computer" else "Player 2")} wins the game!")