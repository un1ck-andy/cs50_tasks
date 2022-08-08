# prompts the user for a date, anno Domini, in month-day-year order,
#  formatted like 9/8/1636 or September 8, 1636,

def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split("/")
            if month.endswith(" ") or day.endswith(" "):
                main()
            if 0 < int(month) < 13 and 0 < int(day) <= 31:
                break
        except:
            try:
                if "," in date:
                    date = date.replace(",", "")
                else:
                    main()
                month, day, year = date.split()
                month = list.index(months, month)+1
                if 0 < int(month) < 13 and 0 < int(day) <= 31:
                    break
            except ValueError:
                pass
            except:
                print()
                pass

    print(f"{year}-{int(month):02}-{day.zfill(2)}")


if __name__ == "__main__":
    main()