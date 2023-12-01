# do the game Rock papper scissors using the user input and a random computer choice

import random

# get the user input
user_choice = input('Enter your choice (rock/paper/scissors): ')

user_say = 'yes'

# make a list of the choices
choices = ['rock', 'paper', 'scissors']

# get the computer choice
computer_choice = random.choice(choices)

# while the user input is  valid and the users want to play compare the choices and count the games and victories of user and print them at the end of game
#count the games and victories of user
games = 0
victories = 0
if user_choice not in choices:
        print('Invalid input, please enter rock, paper, or scissors.')
        user_choice = input('Enter your choice (rock/paper/scissors): ')

while user_choice in choices and user_say == 'yes':
    # count the games
    games += 1
    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('You lose!', computer_choice, 'covers', user_choice)
        else:
            print('You win!', user_choice, 'smashes', computer_choice)
            # count the victories
            victories += 1
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('You lose!', computer_choice, 'cut', user_choice)
        else:
            print('You win!', user_choice, 'covers', computer_choice)
            # count the victories
            victories += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('You lose...', computer_choice, 'smashes', user_choice)
        else:
            print('You win!', user_choice, 'cut', computer_choice)
            # count the victories
            victories += 1

    print('Do you want to play again?')
    # if the user input is yes play again
    user_say = input('Enter yes or no: ')
    if user_say == 'yes':
        user_choice = input('Enter your choice (rock/paper/scissors): ')
        computer_choice = random.choice(choices)
        # if the user input is no print a message
    elif user_say == 'no':
        print('Thanks for playing!')
        # print the games and victories of user
        print('You played', games, 'games and won', victories, 'of them.')
        break
