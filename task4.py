# Ask the user to enter the price
price = float(input("Enter the price: "))

# Ask the user to enter the discount percent
discount_percent = float(input("Enter the discount (%): "))

# Calculate the final price after discount
final_price = price - (price * discount_percent / 100)

# Print the result
print("Price after discount:", final_price)