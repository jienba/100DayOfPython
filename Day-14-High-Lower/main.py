from game_data import data
from art import logo, vs
import random

score = 0
print(logo)
celibrity_A = random.choice(data)
celibrity_B = random.choice(data)
while True:
    print(f"Compare A: {celibrity_A['name']}, {celibrity_A['description']}, {celibrity_A['country']}.")
    print(vs)
    print(f"Against B: {celibrity_B['name']}, {celibrity_B['description']}, {celibrity_B['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B' ").upper()

    # Check User answer
    def check_user_anwer(celebrity_a, celebrity_b, user_answer):
        a = celebrity_a['follower_count'] > celebrity_b['follower_count']
        b = celebrity_a['follower_count'] < celebrity_b['follower_count']
        if user_answer == 'A' and a:
            return 1
        elif user_answer == 'B' and b:
            return 1
        else:
            return 0

    # Tracking score
    score += check_user_anwer(celibrity_A, celibrity_B, answer)


    if check_user_anwer(celibrity_A, celibrity_B, answer):
        print(f"You're right! Current score: {score} ")
        celibrity_A = celibrity_B
        celibrity_B = random.choice(data)
        while celibrity_A['name'] == celibrity_B['name']:
            celibrity_B = random.choice(data)

    else:
        print(f"That's wrong. Final score: {score}")
        break