# ​CHALLENGE 6 | PARCEL DELIVERY
# Create a program to calculate the cost of parcel delivery by doing the following:
# 1: Ask the user to enter the weight of the parcel in kg.
# 2: Ask the user to enter the height of the parcel in cm.
# 3: Ask the user to enter the width of the parcel in cm.
# 4: Ask the user to enter the length of the parcel in cm.
# 5: IF the height + width + length are greater than 200cm then output ' This parcel is too big, it has been rejected'.
# 6: IF the parcel is less than 5kg then the cost of delivery is $10.00
# 7: For every additional 5kg the parcel weighs add an extra $7.00 to the price
# ​(assign the next price increase when the parcel reaches the next weight increment, 10, 15, 20 etc) 
# 8: Output the total cost of delivery in a user friendly sentence.
# EXAMPLE OUTPUT
# Please enter the weight of the parcel in kg: 12
# ​Please enter the height of the parcel in cm: 50
# Please enter the width of the parcel in cm: 40
# ​Please enter the length of the parcel in cm: 60
# The total cost of sending your parcel is: $24.00

# solution
weight = float(input("Please enter the weight of the parcel in kg: "))
height = float(input("Please enter the height of the parcel in cm: "))
width = float(input("Please enter the width of the parcel in cm: "))
length = float(input("Please enter the length of the parcel in cm: "))

if height + width + length > 200:
    print("This parcel is too big, it has been rejected")
else:
    base_cost = 10.00
    additional_cost = 7.00 * (weight // 5)
    total_cost = base_cost + additional_cost
    print(f"The total cost of sending your parcel is: ${total_cost:.2f}")
