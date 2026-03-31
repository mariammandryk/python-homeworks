nums = [0, 1, 0, 12, 3]

result = []
zero_count = 0

for num in nums:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print(result)