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

# print(guess(10))

# computer guesses
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            # low = high, could be high
            guess = low 
        feedback = input(f'{guess} is too high {H}, too low {L} or correct {C}?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yayy! The computer guessed you number, {guess}, correctly!')            


guess(10)