'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([1,-1,0])
you = int(input("Enter your choice (1 for snake, -1 for water, 0 for gun): "))
computer_choice ="snake" if computer == 1 else "water" if computer == -1 else "gun"
print("Computer chose:", computer_choice)
if(computer==you):
    print("its a draw")
else:
    if (computer == -1 and you == 1):
        print("You Win!")

    elif (computer == -1 and you == 0):
        print("You Lose!")  
    elif (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == 1 and you == 0):
        print("You Win!")

    elif (computer == 0 and you == -1):
        print("You win!")

    elif (computer == 0 and you == 1):
        print("You lose!")

    else:
        print("somthing went wrong")