# CHALLENGE 5 | NUMBER GUESSING GAME
# Create a program to do the following:
# 1: Generate a random number or use the two lines of code below to generate a random number, firstly to import random, secondly to produce a random number and save it in a variable called 'num'.
# #FOR PYTHON CODERS
# import random
# num = random.randint(1,20)
# 2: Ask the user to guess a number.
# ​3: IF the user guesses too high then output 'You guess too high, please guess again'.
# 4: IF the user guesses too low then output 'You guess too low, please guess again'.
# ​5: IF the user guesses correct then output 'You guess correct, well done!'.

import random
num = random.randint(1, 20)
while True:
    try:
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if guess > num:
        print("You guessed too high, please guess again.")
    elif guess < num:
        print("You guessed too low, please guess again.")
    else:
        print("You guessed correctly! Well done!")
        break
