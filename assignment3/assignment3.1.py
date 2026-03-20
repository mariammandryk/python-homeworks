num1 = int(input("Enter first number: "))
action = input("Enter action: ")
num2 = int(input("Enter second number: "))

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "/":
    if num2 == 0:
        print("Division by 0 is not allowed")
    else:
        print(num1 / num2)
else:
    print("Incorrect action")