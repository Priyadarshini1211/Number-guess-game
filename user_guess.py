# Number guessing
import random

guesses = 5

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    attempts = 0

    while guess !=  random_number and attempts < guesses:
        guess = int(input(f"Guess a number between 1 and {x}:"))

        if guess < random_number:
            print("Sorry , guess again. Its too low")
        elif guess > random_number:
            print("Sorry,guess again. Its too high")
        else:
            print(f"Kudos, congratulation!. You have guessed the right number {random_number}")
            print (f"And you got it with {attempts+1} attempts!")
            break



        attempts += 1

        if attempts == guesses:
            print (f"You did not guess it, the number was {random_number}. You lose")

 # Print with the color red.
        print(f"\033[91m You have {-(attempts-5)} guesses left. \033[00m")  
guess(10)
