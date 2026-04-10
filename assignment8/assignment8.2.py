import string


def is_palindrome(text):
    new_text = ""

    for symbol in text.lower():
        if symbol not in string.punctuation and symbol != " ":
            new_text += symbol

    return new_text == new_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("OK")