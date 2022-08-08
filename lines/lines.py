import sys

def main():


    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        print("OK")
        try:
            with open(sys.argv[1]) as file:
                lines = file.readlines() #or can be without this line, just for lines in file:
                rows_count = 0
                for line in lines:
                    if line.isspace():
                        pass
                    elif line.strip().startswith("#"):
                        pass
                    else:
                        rows_count += 1
            print(rows_count)
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
