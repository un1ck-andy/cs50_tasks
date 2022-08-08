import requests
import sys
import json


def main():
    #  a command-line argument the number of Bitcoins, that they would like to buy.
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    #get the json
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        coindesk_json = response.json()
        #find the price inside json
        price = coindesk_json["bpi"]["USD"]["rate_float"]
        #calculate and print sum
        total_price = price * number
        print(f"${total_price:,.4f}")
    except requests.RequestException:
        print("Error with request")


if __name__ == "__main__":
    main()
