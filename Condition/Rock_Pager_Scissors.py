"""
====== Welcome to the game ======
Please enter Rock, Paper, or Scissors below:
Rock
You win! Your opponent chose 'Scissors'

"""

import random
user_c = input("Please enter Rock, Paper, or Scissors below: ")

rps = ("Rock", "Paper", "Scissors" )
com_c = rps[random.randint(0,2)]

flag = None # 1 = win, 2 = lose, 3 
if user_c.lower() == "rock":
    if( com_c == "Paper" ):
        flag = 1
    else:
        flag = 0
elif user_c.lower() == "paper":
    if com_c == "Scissors":
        flag = 0
    else:
        flag = 1
else:
    if( com_c == "Rock" ):
        flag = 0
    else:
        flag = 1

if( flag == 1 ):
    print("You won")
elif (flag == 0 ):
    print("You lose")
else:
    print("Tie")