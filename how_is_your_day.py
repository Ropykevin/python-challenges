
# A: Ask the user If it is sunny, raining or snowing outside
# B: If the user replies ‘sunny’ then output ‘Great, remember your hat’
# C: If the user replies ‘raining’ then output ‘Remember your coat’
# D: If the user replies ‘snowing’ then output ‘Great, remember your ski’s’
# E: if the user replies with any other comment then output ‘ OK, have a good day’
# EXAMPLE OUTPUT
# What is the weather like today?  Sunny
# Great, remember your hat

weather = input("What is the weather like today? ").lower()
if weather == "sunny":
    print("Great, remember your hat")
elif weather == "raining":
    print("Remember your coat")
elif weather == "snowing":
    print("Great, remember your ski’s")
else:
    print("OK, have a good day")

# Adapt you program to work if the user types in any variation of capital letters or lowercase letters.
# HINT: You could use one of the following 3 methods to do this:
# .lower()     .upper()   .title()
weather = input("What is the weather like today? ").lower()
if weather == "sunny":
    print("Great, remember your hat")
elif weather == "raining":
    print("Remember your coat")
elif weather == "snowing":
    print("Great, remember your ski’s")
else:
    print("OK, have a good day")

