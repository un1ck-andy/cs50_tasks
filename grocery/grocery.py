# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase,
#  sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
# Treat the user’s input case-insensitively.

def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except KeyError:
            pass
        except EOFError:
            for x in sorted(grocery_list):
                print(grocery_list[x], x)
            break


if __name__ == "__main__":
    main()