import random

player = int(input("Press 1 for Rock, Press 2 for Paper, Press 3 For scissors. "))
bot = random.randint(1,3)

if player == 1:
    print("You picked Rock.")
elif player == 2:
    print("You picked Paper.")
elif player == 3:
    print("You picked Scissors.")
elif player <= 4:
    print("That wasn't an option.")


if bot == player:
    print("That one was a tie.")
elif bot == 1:
    if player == 2:
        print("I picked Rock. You picked Paper. You Win!")
    elif player == 3:
        print("I picked Rock. You picked Scissors. I Win!")
elif bot == 2:
    if player == 3:
        print("I picked Paper. You picked scissors. You Win!")
    elif player == 1:
        print("I picked Paper. You picked Rock. I Win!")
elif bot == 3:
    if player == 1:
        print("I picked Scissors. You picked Rock. You Win!")
    elif player == 2:
        print("I picked Scissors. You picked Paper. I Win!")