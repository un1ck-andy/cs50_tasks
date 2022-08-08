import os, sys
from PIL import Image, ImageOps


def main():
    check_args()
    check_extension()

    try:
        our_image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        our_image = ImageOps.fit(our_image, size, bleed=0.0, centering=(0.5, 0.5))
        our_image.paste(shirt,shirt)
        our_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def check_extension():
    path_1 = os.path.splitext(sys.argv[1])
    path_2 = os.path.splitext(sys.argv[2])
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if path_1[1] not in valid_extensions:
        sys.exit("Invalid output")
    elif path_1[1] != path_2[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
