import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if valid := re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip):
        pass
    else:
        return False
    ip_list = ip.split(".")
    for number in ip_list:
        if int(number) < 256:
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    main()
