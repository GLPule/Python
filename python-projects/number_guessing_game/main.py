import random

play = True
scores = []
best_score = 9999
game = 7
while play:
    user_start = input("Enter 'quiet' to end the game. Do you want to start the game: ").strip().lower()
    if user_start == "quiet":
        play = False
    else:
        try:
            min = int(input("Enter the minimum number: "))
            max = int(input("Enter the maximum number: "))
        except ValueError:
            print("Invalid input!!. Only integers are allowed")
            quit()
        num = random.randint(min,max)
        attempts = game
        attempt = 0
        while play:
            try:
                print(f"You have {attempts} attempts to guess the correct number")
                user = int(input(f"Guess the number (between {min}-included and {max}-included): "))
                attempts -= 1
                attempt += 1
                if user < min or user > max:
                    print(f"\tThe number must be between {min} and {max}!!")
                else:
                    if user == num:
                        print(f"\tCongratulations! You guessed the number with {attempt} attempts.")
                        scores.append(attempt)
                        if scores != []:                           
                            for score in scores:
                                if score < best_score:
                                    best_score = score
                            print(f"Best Score: {best_score}/{game}")
                        break
                    elif attempts == 0:
                        print(f"\tGame Over! The correct number is {num}")
                        break
                    elif user > num:
                        print("\tToo high! Try again.")
                    else:
                        print("\tToo low! Try again")
            except ValueError:
                print("\tInvalid input!!. Only numbers are allowed")


    

    
    