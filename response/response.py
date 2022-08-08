from validators import email


def main():
    print(email_check(input("What's your email address?: ")))


def email_check(s):
    if email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
