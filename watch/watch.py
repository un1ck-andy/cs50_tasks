import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.match(r'<iframe.*?src="https?://(?:www.)?youtube\.com/embed/(\w+?)".*?></iframe>', s):
        return(f"https://youtu.be/{link[1]}")
    else:
        return None


if __name__ == "__main__":
    main()
