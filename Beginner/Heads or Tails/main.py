import random

decider_number = random.randint(1, 100)

if decider_number % 2:
    print("Heads")
else:
    print("Tails")
