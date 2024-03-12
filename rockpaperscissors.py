#This code allows the user to play a game of rock-paper-scissors against the computer. 
#It randomly selects the computer's choice, prompts the user for their choice, compares the choices, and determines the outcome, printing whether the user wins, loses, or ties with the computer.

import random

computer_choice = random.choice(['rock','paper','scissors']);
user_choice = input('Do you want rock, paper, or scissors?\n');
print('computer choice:'+ computer_choice);

if computer_choice == user_choice:
    print("tie");
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("win")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("win")
else:
    print('you lose');

#using the python standard library
