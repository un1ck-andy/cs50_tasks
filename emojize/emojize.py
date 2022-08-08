from emoji import emojize

def main():
    user_input = input("Input: ")
    output = emojize(user_input)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()