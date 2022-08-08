def main():
    amount = 50
    while True:
        amount = amount - get_coin(amount)
        if amount <= 0:
            print(f"Change owed: {-amount}")
            break

def get_coin(amount):
    while True:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            return coin

if __name__ == "__main__":
    main()