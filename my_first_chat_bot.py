# Create a program to do the following:
# 1: Ask the user their name and store the answer in a variable.
# 2: Use the users name in a response and ask the user what day it is and save the answer in a variable.
# 3: Ask the user what the weather is like. Give some prompts for response for example' Rainy', 'Cloudy', 'Sunny', 'Hot', 'Cold'. 
# 4: Return a statement to the user to wish them a happy day, use all data saved in your variables in the response.
# When you run your program it should look something like the output shown below.
# EXAMPLE OUTPUT
# Hello what is your name? Bob
# Hello Bob, what day is it today? Monday
# And what is the weather like today? Sunny
# Ok Bob, I hope you enjoy your day on this Sunny Monday

user_name = input("Hello, what is your name? ")
day_of_week = input(f"Hello {user_name}, what day is it today? ")
weather_prompt = "What is the weather like today? (Rainy/Cloudy/Sunny/Hot/Cold): "
weather = input(weather_prompt)
output_message = f"Ok {user_name}, I hope you enjoy your day on this {weather} {day_of_week}"
print(output_message)
