import random

decider_number = random.randint(1, 100)
print(decider_number)

if decider_number % 2:
    print("Heads")
else:
    print("Tails")
