from os import system, name
from art import logo

print(logo)
print("Welcome to the secret auction program")


def clear():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Methode 1: dictionary in dictionary

bids = {}
is_bidder_rest = True


def highest_bid(bid_dictionary):
    max_amount = 0
    winner = " "
    for bid in bid_dictionary:
        if bid_dictionary[bid] > max_amount:
            max_amount = bid_dictionary[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of {max_amount}")


while is_bidder_rest:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    bidder_rest = input("Are there any other bidders ").lower()

    if bidder_rest == 'yes':
        clear()
    elif bidder_rest == 'no':
        is_bidder_rest = False
        highest_bid(bids)

"""
# Method 2: dictionary in list
bidders = []
is_bidder_rest = True


def add_bidder(name, price):
    bidders.append(
        {
            "name": name,
            "price": price
        }
    )


def max_bidder(bidders_arr):
    max_price = 0
    winner = ''
    for bidder in bidders_arr:
        if bidder['price'] > max_price:
            max_price = bidder['price']
            winner = bidder['name']

    print(f"The winner is {winner} with a bid of {max_price}")


print(logo)
print("Welcome to the secret auction program")
name = " "
price = 0

while is_bidder_rest:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))

    add_bidder(name, price)
    others_bidders = input("Are there any other bidders ").lower()

    if others_bidders == 'yes':
        clear()
        add_bidder(name, price)
    elif others_bidders == 'no':
        max_bidder(bidders)
        is_bidder_rest = False
"""
