def common_elements():
    numbers1 = {number for number in range(100) if number % 3 == 0}
    numbers2 = {number for number in range(100) if number % 5 == 0}

    return numbers1 & numbers2


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")