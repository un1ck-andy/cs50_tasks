def main():
    inp = input("Input: ")
    output = shorten(inp)
    print(f"Output: {output}")


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in range(len(vowels)):
        word = word.replace(vowels[i], "")
    return(word)


if __name__ == "__main__":
    main()
