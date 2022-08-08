import sys
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as csvfile:
                reader = csv.DictReader(csvfile)
                table = []
                for row in reader:
                    table.append({"full_name": row["name"], "house": row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        after_table = []
        for row in table:
            last, first = str.split(row["full_name"], ",")
            after_table.append({"first": first.strip(), "last": last, "house": row["house"]})

        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in after_table:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()
