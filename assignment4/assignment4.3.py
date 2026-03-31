import random

numbers = []
size = random.randint(3, 10)

for i in range(size):
    numbers.append(random.randint(1, 10))

result = [numbers[0], numbers[2], numbers[-2]]

print(numbers)
print(result)