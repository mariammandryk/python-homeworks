import string

letters = input("Enter two letters with hyphen: ")

start = letters[0]
end = letters[2]

all_letters = string.ascii_letters

start_index = all_letters.index(start)
end_index = all_letters.index(end)

result = all_letters[start_index:end_index + 1]

print(result)