def main():
    inp = input("Input: ")
    output = twttr(inp)
    print(f"Output: {output}")


def twttr(inp):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in range(len(vowels)):
        inp = inp.replace(vowels[i], "")
    return(inp)

# more sophisticated version
# cleaned = ['' if char in vowels else char for char in inp]

# cleaned = []
# for char in inp:
#     cleaned.append('' if char in vowels else char)


if __name__ == "__main__":
    main()
