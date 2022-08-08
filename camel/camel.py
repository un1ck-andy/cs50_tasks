camel = input("camelCase: ")
print("snake_case: ", end="")

for character in camel:
    if character.isupper():
        print(f"_{str.lower(character)}", end="")
    else:
        print(character, end="")

print()