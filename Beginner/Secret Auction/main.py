from art import gavel

bid_on = True
people_bids = {}
highest_bid = 0
winner = ""

print(gavel)

while bid_on:
    print("Welcome to the Secret Auction")

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()

    people_bids[name] = bid

    if more_bidders == "yes":
        for i in range(50):
            print("\n")
    elif more_bidders == "no":
        for key in people_bids:
            if people_bids[key] > highest_bid:
                highest_bid = people_bids[key]
                winner = key
                bid_on = False
            else:
                pass
        print(f"\nThe winner is {winner} with a bid of {highest_bid}!")
