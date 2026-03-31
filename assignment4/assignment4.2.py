nums = [0, 1, 7, 2, 4, 8]

if len(nums) == 0:
    print(0)
else:
    sum_even_index = 0

    for i in range(0, len(nums), 2):
        sum_even_index += nums[i]

    result = sum_even_index * nums[-1]
    print(result)