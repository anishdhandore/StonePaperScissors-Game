import random
import math

mylist = ["rock", "paper",  "scissor"]

run = True
while run:

    player = input("Rock/Paper/Scissor? ")
    item = random.choice(mylist)

    if player.lower() == item:
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("IT IS A TIE!")
    # conditions when player wins
    elif player.lower() == "rock" and item == "scissor":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU WIN!")

    elif player.lower() == "paper" and item == "rock":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU WIN!")

    elif player.lower() == "scissor" and item == "paper":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU WIN!")
    # conditions when player loses
    elif player.lower() == "rock" and item == "paper":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU LOSE!")

    elif player.lower() == "paper" and item == "scissor":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU LOSE!")

    elif player.lower() == "scissor" and item == "rock":
        print("Player : {}".format(player))
        print("Computer : {}".format(item))
        print("YOU LOSE!")

    else:
        print("Enter only rock/paper/scissor?")
        play_again = input("Do you want to play again, yes or no? ")

        # if player says no, then we say the loop is false
        if play_again.lower() == "no":
            run = False
        
        # if  yes, then we skip step by using continue
        else:
            continue
    
       
