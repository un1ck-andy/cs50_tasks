import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    #old version
    # ums = 0
    # text = s.split(" ")
    # for line in text:
    #     if re.findall(r"^um\b", line, re.I):
    #         ums += 1
    # return(ums)

    #updated
    ums = re.findall(r"\b(um)\b", s, re.I)
    return len(ums)

if __name__ == "__main__":
    main()
