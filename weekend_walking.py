# Create a program to do the following:
# 1: Ask the user their name and store the answer in a variable.
# 2: Ask the user how many kilometers they walked on Saturday and store in a variable.
# 3: Ask the user how many kilometers they walked on Sunday and store in a variable.
# 4: Add the kilometers walked on Saturday and Sunday together and store in a new variable.
# 5: Output to the user, in a sentence, the total kilometer walked.
# ​
# EXAMPLE OUTPUT
# Hello what is your name? Bob
# Hello Bob, how many kilometers did you walk on Saturday? 10
# Ok Bob, how many kilometers did you walk on Sunday? 7
# Great walking Bob, that means you walked a total of 17 kilometers this weekend.
user_name = input("Hello, what is your name? ")
kilometers_saturday = float(input(f"Hello {user_name}, how many kilometers did you walk on Saturday? "))
kilometers_sunday = float(input(f"Ok {user_name}, how many kilometers did you walk on Sunday? "))
total_kilometers = kilometers_saturday + kilometers_sunday
print(f"Great walking {user_name}, that means you walked a total of {total_kilometers} kilometers this weekend.")
