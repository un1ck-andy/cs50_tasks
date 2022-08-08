import inflect


def main():
    # start inflect to use it method
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            names_str = p.join((names))
            print(f"Adieu, adieu, to {names_str}")
            break


if __name__ == "__main__":
    main()
