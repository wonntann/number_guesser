import random

def guess(x):
    random_number = random.randint(1, x)
    # start guess at 0 value
    guess = 0
    # while expression
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        # return guess  # Test it
        # conditional
        if guess < random_number:
            print ('Sorry, guess again. Too low.')
        elif guess > random_number:
            print ('Sorry, guess again. Too high.')
        else:
            print ('You got it right!') 

# input the maximum number value to guess
guess(10)