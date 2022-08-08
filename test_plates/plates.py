def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# “All vanity plates must start with at least two letters.”
    if str.isdigit(s[0:2]) == True:
        return False

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

# “Numbers cannot be used in the middle of a plate; they must come at the end.
    for char in range(len(s)):
        if s[char].isdigit():
            if not s[char:].isdigit():
                return False

# The first number used cannot be a ‘0’.”
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

# “No periods, spaces, or punctuation marks are allowed.”
    if s.isalnum() == False:
        return False
    return True


if __name__ == "__main__":
    main()
