def main():
    try:
        fuel = convert(input("Fraction: "))
    except (NameError, ZeroDivisionError, ValueError):
        pass
    fuel = gauge(fuel)
    print(fuel)

def convert(fraction):
    x, y = str.split(fraction, "/")
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    tank = round(float(x) / float(y) * 100)
    return tank


def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return f"E"
    elif 99 <= percentage <= 100:
        return f"F"


if __name__ == "__main__":
    main()
