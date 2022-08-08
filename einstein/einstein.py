def energy(m):
    x = int(m) * pow(300000000, 2)
    return x


def main():
    e = energy(input("m: "))
    print("E: ", e)


if __name__ == "__main__":
    main()