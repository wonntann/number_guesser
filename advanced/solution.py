# python random and time module
import random, time

# main guessing function
def guess():

    # start guess at 0 value
    guess = 0

    # while True loop to handle exceptions and incorrect input
    while True:
        # get user input and convert data type to integer
        try:
            x = int(input("Enter the maximum number that you want to guess up to: "))
        except:
            print("Please input a numeric digit")
            # continue game if the input is correct
            continue
            

        # pause game before starting
        time.sleep(1)

        # generate the random number 
        random_number = random.randint(1, x)

        # while expression to loop game while guess doesn't equal the number
        while guess != random_number:
            # get user input, place the max number
            guess = int(input(f"Guess a number between 1 and {x}: "))

            # compare the guess to the randomly generated number
            if guess < random_number:
                print ("You guessed a little too high")
            elif guess > random_number:
                print ("You guessed a little too high")
            else:
                print ("You got it right!") 


# execute the main function
guess()