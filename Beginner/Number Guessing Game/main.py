import random
from art import logo

game_on = True

attempts = 0

num_2_guess = random.choice(range(1, 101))

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number from 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts =10
    print(f"\nYou have {attempts} remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print(f"\nYou have {attempts} remaining to guess the number.")
else:
    print("Invalid input.")
    game_on = False

def check_ggs():
    global game_on
    if attempts == 0:
        print(f"\nThe number was {num_2_guess}.")
        print("You've run out of guesses. You lose :(")
        game_on = False
        return 0

def num_guess():
    global attempts, game_on
    guess = int(input("Make a guess: "))
    if guess < num_2_guess:
        print("\nToo low.")
        attempts -= 1
        if check_ggs() == 0:
            return
        print("Guess again.\n")
        if attempts > 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif attempts == 1:
            print(f"You have {attempts} attempt remaining to guess the number.")
        num_guess()
    elif guess > num_2_guess:
        print("\nToo high.")
        attempts -= 1
        if check_ggs() == 0:
            return
        print("Guess again.\n")
        if attempts > 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif attempts == 1:
            print(f"You have {attempts} attempt remaining to guess the number.")
        num_guess()
    elif guess == num_2_guess:
        print(f"\nYou guessed it! The number was {num_2_guess}!\nYou win! =D")
        game_on = False


while game_on:
    num_guess()
