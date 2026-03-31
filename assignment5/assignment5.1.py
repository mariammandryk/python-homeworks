import keyword

name = input("Enter variable name: ")

if len(name) == 0:
    print(False)
elif name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif not name.islower():
    print(False)
elif "__" in name:
    print(False)
else:
    is_valid = True

    for symbol in name:
        if not (symbol.islower() or symbol.isdigit() or symbol == "_"):
            is_valid = False
            break

    print(is_valid)