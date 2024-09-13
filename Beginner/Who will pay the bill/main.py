import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Using randint
print(f"The person who has to pay the bill is {friends[random.randint(0,4)]}!")

# Using random.choice
print(f"The person who has to pay the bill is {random.choice(friends)}!")
