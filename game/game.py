from random import randint


def main():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input <= 0:
                pass
            else:
                break
        except:
            pass

    number = randint(1, level_input)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except:
            pass


if __name__ == "__main__":
    main()
