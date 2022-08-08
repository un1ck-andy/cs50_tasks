import inflect
from datetime import date
import sys


def main():
    birth_date = get_birth_date(input("Date of Birth: "))
    minutes = calculate_minutes(birth_date)
    print(print_minutes_words(minutes))


# get and check year
def get_birth_date(d):
    try:
        year, month, day = d.split("-")
        birth_date = date(int(year), int(month), int(day))
        return birth_date
    except:
        sys.exit("Invalid")


# calculate minutes
def calculate_minutes(birth_date):
    delta = birth_date - date.today()
    minutes = -delta.days * 1440
    return minutes


# print
def print_minutes_words(minutes):
    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="").capitalize()
    return f"{minutes_in_words} minutes"


if __name__ == "__main__":
    main()
