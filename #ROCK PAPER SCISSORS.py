#ROCK PAPER SCISSORS
import random

weapon = ["rock", "paper", "scissors"] #list of weapons for computer to choose from

computer = random.choice(weapon) #this function will randomise what the computer will pick from weapons list

print("!!! welcome to this game of rock sham bow !!!!" )

player_one = input("choose your weapon!!! rock, paper or scissors \U0001F600 ---") #the input function will get user input 



if player_one == "rock" and computer == "scissors":
    print(f"computer plays {computer}")
    print("player one wins!")
       
elif player_one == "scissors" and computer == "paper":
    print(f"computer plays {computer}")
    print("player one wins!")
     
elif player_one == "paper" and computer == "rock":
    print(f"computer plays {computer}")
    print("player one wins!")

elif computer == "rock" and  player_one == "scissors":
    print(f"computer plays {computer}")
    print("computer wins!")
    
elif computer == "scissors" and player_one == "paper":
    print(f"computer plays {computer}")
    print("computer wins!")
        
elif computer == "paper" and player_one == "rock":
    print(f"computer plays {computer}")
    print("computer wins!")
        
elif player_one == computer:
    print(f"computer plays {computer}")
    print("its a draw")







