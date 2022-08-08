def convert(text):
    faces = text.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces


def main():
    print(convert(input("")))


if __name__ == "__main__":
    main()