"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import mean
from statistics import median
from statistics import mode

guesses =[]

def start_game():
    
    
    print('***** Welcome to the number guessing game ****')
    
    
    
    name = input("What is your name? ")
    
    if len(guesses) == 0:
        print(f"Hey,{name},High score is up for the grabs.Best of luck")
    else:
        print(f"Hey,{name},The current high score to beat is {min(guesses)}")
    
    answer = random.randint(1,100)
    total_guesses = 0
    
    game_running = True
    
    while game_running:
        
        total_guesses +=1
        try:
            guess=  int(input("Please enter a number between 1-100 "))
            if guess < 1 or guess > 100:
                raise ValueError
            elif guess >answer:
                print('Its lower')
            elif guess< answer:
                print('Its higher' )
            else:
                print(f'You guess the right number,and it took you {total_guesses} attempts')
                game_running = False
                guesses.append(total_guesses)
                print("**Overall Statistics**")
                print(f"Mean:{mean(guesses)}")
                print(f"Mode:{mode(guesses)}")
                print(f"Median:{median(guesses)}")
    
        except ValueError:
            print("Your guess is out of range. Please chose a number between 1 and 100")
    
    play_again = input("Play again? Y/N ")
    if play_again.upper() == "Y":
        start_game()
    elif play_again.upper() == "N":
        print("thank you for playing")
        
        
        
        




# Kick off the program by calling the start_game function.
start_game()