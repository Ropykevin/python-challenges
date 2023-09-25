# A local bake sale wants to sell the following:
# 1: Pie's at $4 each
# 2: Muffin's at $3 each
# 3: Donut's at $2 each
# Can you create a program to help them calculate the bill for each customer. 

# Create a program to do the following:
# 1: Ask the customer how many pie's they want to buy.
# 2: Create a subtotal cost for the total cost of pie's the customer wants.
# 3: Ask the customer how many Muffin's they want to buy.
# 4: Create a subtotal cost for the total cost of Muffin's the customer wants.
# 5: Ask the customer how many Donut's they want to buy.
# 6: Create a subtotal cost for the total cost of Donut's the customer wants.
# 7: Add the subtotals and output the total value of the purchase.

num_pies = int(input("How many pies would you like to buy? "))
pie_price = 65  
pie_subtotal = num_pies * pie_price

num_muffins = int(input("How many muffins would you like to buy? "))
muffin_price = 45  
muffin_subtotal = num_muffins * muffin_price

num_donuts = int(input("How many donuts would you like to buy? "))
donut_price = 25  
donut_subtotal = num_donuts * donut_price

total_cost = pie_subtotal + muffin_subtotal + donut_subtotal
print(f"Your total bill is ${total_cost:.2f}")
