def main():
    tank = get_tank()
    if 1 < tank < 99:
        print(f"{tank}%")
    elif tank <= 1:
        print("E")
    elif 99 <= tank <= 100:
        print("F")
    else:
        tank = get_tank()


def get_tank():
    while True:
        try:
            x, y = str.split(input("Fraction: "), "/")
            tank = round(int(x) / int(y) * 100)
            return tank
        except (NameError, ZeroDivisionError, ValueError):
            pass


if __name__ == "__main__":
    main()
