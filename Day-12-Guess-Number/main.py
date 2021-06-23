from random import randint

# jienba version
"""
print("Welcome to the number guessing game")
print("I'm thinking a number between 1 and 100")
# 1. Generate random number between 1 and 100

number_to_guess = random.choice(range(1, 101))

# 2. Choosing a difficulty

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(f"The number to guess is {number_to_guess}")

if difficulty == 'hard':
    attempts = 5
else:
    attempts = 10
number = 0

while number != number_to_guess or attempts < 1:
    print(f"You have {attempts} attempts remaining to guess the number")
    number = int(input("Make a guess: "))
    attempts -= 1
    if number < number_to_guess:
        print("Too low")
    elif number > number_to_guess:
        print("Too high")
    if attempts < 1:
        print("You've run out of guesses. You lose")
if number == number_to_guess:
    print(f"You got it. The answer was {number_to_guess}.")
    """
# jienba optimized
print("Welcome to the Number guessing game")
print("I'm thinking of a number between 1 and 100")
# Choosing a random number between 1 and 100
number_to_guess = randint(1, 100)

TURNS_FOR_HARD_LEVEL = 5
TURNS_FOR_EASY_LEVEL = 10


# Function to check user's guess against actual answer and track the number of turns and reduce by 1 if they get  it
# wrong

def check_user_answer(guess, answer, attempts):
    if guess == answer:
        print(f"You got it. The number to guess was {answer}")
        return 0
    elif guess > answer:
        print("Too high")
        return attempts - 1
    else:
        print("Too low")
        return attempts - 1


# Make function to set difficulty
def set_difficulty():
    level = input("Choose your difficulty. Type 'easy' or 'hard': ")
    if level == 'hard':
        return TURNS_FOR_HARD_LEVEL
    elif level == 'easy':
        return TURNS_FOR_EASY_LEVEL


# Let the user the user guess a number
turns = set_difficulty()
number = 0
# Repeating the guessing functionality  if they get it wrong
while number != number_to_guess:
    print(f"You have {turns} attempts remaining to guess the number.")
    number = int(input("Make a guess: "))
    turns = check_user_answer(number, number_to_guess, turns)
    if turns < 1:
        print("You've run out of guesses. You lose ")
        break
