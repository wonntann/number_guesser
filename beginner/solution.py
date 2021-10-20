# python random module
import random

# number of variables
attempts = 0

# choose a random number
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# while the player's guesses is less then 6
while attempts < 6:
    guess = input("Take a guess: ")
    guess = int(guess)

    attempts += 1

    # if the player's guess is too low
    if guess < number:
        print("You guessed a little too low")

    # if the player's guess is too high
    if guess > number:
        print("You guessed a little too high")
        
    # if the player won, stop the loop
    if guess == number:
        break

# if the player won
if guess == number:
    attempts = str(attempts)
    print(f"Good job! You guessed my number in {attempts} guesses!")

# if the player lost
if guess != number:
    number = str(number)
    print(f"Nope. The number I was thinking of was {number}")