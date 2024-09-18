def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    for letters in name1 + name2:
        if letters in "true":
            score1 += 1
        if letters in "love":
            score2 += 1
    print(f"Your true love score is: {score1}{score2}.")


calculate_love_score(input("What is the first person's first and last name?\n").lower(),
                     input("What is the second person's first and last name?\n").lower())
