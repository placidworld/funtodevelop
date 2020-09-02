# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:32:11 2020

@author: heart
"""

# import the extra Python functions we'll need for the code - they're still parts of the standard Python libraries
# just not part of the default environment

import random
import time

rock = 1
paper = 2
scissors = 3

# the initial rules of the game are created here. The three variables we're using and their relationship
# is defined. We also provide a variable so we can keep score of the games

names = {rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

# begin the code by defining the start of each round. The end of each play session comes back through here, 
# whether we want to play again or not
"""
The pass statement allows the while loop to stop once we've finished, and could be used to perform a number of 
other tasks if so wished. 
"""

def start():
    print("Let's play a game of Rock, Paper, Scissors")
    while game():
        pass
    scores()


"""
The game is actually contained all in here, asking for the players to input, getting the computer input 
and passing these on to get the results. at the end of that, it then asks if you'd like to play again
"""

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        
        print("Oops! I did't understand that. Please enter 1, 2 or 3")
        
        
"""
The result function here only takes the variables player and computer for this task, which is why we set 
that in result(player, computer).
Also here we are starting off by having a countdown to the result. 
"""

def result(player, computer):
    print ("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs as you realize you have been defeated.")
            computer_score +=1
            
"""
Ask for text input on whether or not someone wants to play again. Depending on their response, we go 
back to the start, or end the game and display the results.
"""

def play_again():
    answer = input("Would you like to play again? y/n:  ")
    if answer in ("y", "Y", "Yes", "YES", "Of course"):
        return answer
    else:
        print("Thank you very much f or playing our games. See you next time.")
        
def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)
    
if __name__ == '__main__':
    start()