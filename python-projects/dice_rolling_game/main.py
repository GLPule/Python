'''
Ask user how many dice they want to roll,
then generate dice based on user input and
display the results.
'''

import random
def die_creator(dice):                  #Create dice based on user input
    dice_list = []
    for die in range(dice):
        roll = random.randint(1,6)             
        dice_list.append(roll)
    return dice_list
          
try:
    dice = int(input("How many dice to you want to roll: "))
    if dice == 0:
        print("You can't roll 0 dice")
        quit()
except ValueError:
    print("Invalid input!!.Only numbers are allowed")
    quit()

count = 0

while True: 
    user = input("Roll the dice? (y/n): ").strip().lower()
    if user == "n":
        print("Thanks for playing the game.")
        break
    elif user != "y":
            print("Invalid Choice!! Try Again")
    else:
        count += 1
        print(f"Rolling: {count}")
        print(die_creator(dice))




