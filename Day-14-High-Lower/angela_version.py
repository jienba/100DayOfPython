from os import system, name
from art import logo, vs
from game_data import data
import random


def clear():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def format_data(account):
    """Take the account data and return  printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, {account_country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """Take the user guess and follower counts and return if they got it right"""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


score = 0
# Display art logo
print(logo)

game_should_continue = True
# Make game repeatable
account_b = random.choice(data)
while game_should_continue:
    # Making account at position B become next account at position A.
    # Generate  a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()
    print(logo)
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
