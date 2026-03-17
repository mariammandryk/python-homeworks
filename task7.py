# Ask the user to enter a four-digit number
number = int(input("Enter a four-digit number: "))

# Find each digit
digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10

# Print each digit on a new line
print(digit1)
print(digit2)
print(digit3)
print(digit4)