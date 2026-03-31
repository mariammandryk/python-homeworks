import string

text = input("Enter text: ")

new_text = ""

for symbol in text:
    if symbol not in string.punctuation and symbol != " ":
        new_text += symbol
    else:
        new_text += " "

words = new_text.split()

result = "#"

for word in words:
    result += word.capitalize()

if len(result) > 140:
    result = result[:140]

print(result)