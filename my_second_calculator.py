# Create a program to do the following:

# 1: Ask the use what type of calculation they would like to do 1: Add  2: Subtract  3: Multiply
# 2: Ask the user to enter a number
# ​3: Ask the user to enter another number
# 4: Create a variable to hold the answer and perform the appropriate calculation
# ​5: Output the answer in a user-friendly sentence.
# Step 1: Ask the user what type of calculation they would like to do
print("Choose a calculation:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")

choice = input("Enter your choice (1/2/3): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == '1':
    result = num1 + num2
    operation = "addition"
elif choice == '2':
    result = num1 - num2
    operation = "subtraction"
elif choice == '3':
    result = num1 * num2
    operation = "multiplication"
else:
    print("Invalid choice")
    exit()
print(f"The result of {num1} and {num2} {operation} is: {result}")
