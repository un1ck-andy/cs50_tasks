from pyfiglet import Figlet
import sys
from random import randint


def main ():
    figlet = Figlet()
    fonts = figlet.getFonts()

# check args
    if len(sys.argv) > 1:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else: #no args = random font
        font = fonts[randint(1, len(fonts))]

    text = input("Input: ")
    print(f"Output: ")
    figlet = Figlet(font=font)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()