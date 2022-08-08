# value expects a str as input and returns 0 if that str starts with “hello”,
# 20 if that str starts with an “h” (but not “hello”), or
# 100 otherwise,
# treating the str case-insensitively.
# Only main should call print.

def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print(f"${money}")

def value(greeting):
    greeting = str.strip(str.casefold(greeting))
    if str.startswith(greeting, "hello"):
        return 0
    elif str.startswith(greeting, "h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
