try:
    x, y, z = str.split(input("Expression: "))
except NameError as error:
    print("Please enter full expression, e.g. 1 + 1")
except ValueError as error:
    print("Please enter full expression, e.g. 1 + 1")

if y == "/" and z == "0":
    print("You can't divide by zero")

elif y == "+":
    print(float(x) + float(z))

elif y == "-":
    print(float(x) - float(z))

elif y == "*":
    print(float(x) * float(z))

elif y == "/" and z != "0":
    print(float(x) / float(z))
