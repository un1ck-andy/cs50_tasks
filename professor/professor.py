import random


def main():
    total = 0
    score = 0
    # getting level by cycle
    level = get_level()
    # setting 10 math
    while total < 10:
        integer_1 = generate_integer(level)
        integer_2 = generate_integer(level)
        errors = 0
        # checking answer cycle
        while errors <= 3:
            # if it's 3d error
            if errors == 3:
                print(f"{integer_1} + {integer_2} = {answer}")
                break
            user_answer = int(input(f"{integer_1} + {integer_2} = "))
            answer = integer_1 + integer_2
            if user_answer != answer:
                print("EEE")
                errors += 1
            else:
                score += 1
                break
        total += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            else:
                break
        except ValueError:
            pass

    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
