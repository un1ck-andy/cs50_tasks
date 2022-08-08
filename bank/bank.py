greeting = input("Greeting: ")
greeting = str.strip(str.casefold(greeting))


if str.startswith(greeting, "hello"):
    print("$0")
elif str.startswith(greeting, "h"):
    print("$20")
else:
    print("$100")

