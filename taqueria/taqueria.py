menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    price = 0
    while True:
        try:
            item = str.title(input("Item: "))
            if item in menu:
                price = float(price) + menu[item]
                print(f"Total: ${price:.2f}")
        except (KeyError):
            pass
        # Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()
