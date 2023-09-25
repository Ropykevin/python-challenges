# Create a program using a single IF, then, else statement to do the following:
# A: Ask the user for a test score 0 - 100:
# B: If the test score is greater than 80 the output - Your Grade is: A
# C: If the test score is greater than 60 the output - Your Grade is: B
# D: If the test score is greater than 50 the output - Your Grade is: C
# E: If the test score is greater than 40 the output - Your Grade is: D
# F: If the test score is less than 40 the output - Your Grade is: E

test_score = int(input("Enter your test score (0 - 100): "))
if test_score > 80:
    grade = "A"
elif test_score > 60:
    grade = "B"
elif test_score > 50:
    grade = "C"
elif test_score > 40:
    grade = "D"
else:
    grade = "E"

print(f"Your Grade is: {grade}")
