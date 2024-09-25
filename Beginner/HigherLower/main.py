import random
from art import logo, vs
from data import data
game_on = True
score = 0
already_used = []

account1 = data[random.randint(0, 49)]
already_used.append(account1)


def check_same_account(ac1, ac2):
    while ac1 == ac2:
        ac2 = data[random.randint(0, 49)]
    return ac2

def check_if_used(account):
    while account in already_used:
        account = data[random.randint(0, 49)]
    return account

def play():
    global score, game_on, account1

    if len(already_used) >= len(data):
        print("No more accounts left to play. Thanks for playing!")
        game_on = False
        return

    higher_followers = {}

    account2 = data[random.randint(0, 49)]
    account2 = check_same_account(ac1=account1, ac2=account2)
    account2 = check_if_used(account=account2)

    if account1["follower_count"] > account2["follower_count"]:
        higher_followers = account1
    elif account1["follower_count"] < account2["follower_count"]:
        higher_followers = account2

    print(f"Compare A: {account1['name']}, a {account1['description']} from {account1['country']}.")
    print(vs)
    print(f"Against B: {account2['name']}, a {account2['description']} from {account2['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == "a":
        guess = account1
    elif guess == "b":
        guess = account2

    if guess == higher_followers:
        score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score: {score}.")
        account1 = higher_followers
        already_used.append(account2)
        play()
    elif guess != higher_followers:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_on = False


print(logo)

while game_on:
    play()
