from ascii import list_o_ascii
import random

player_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

# For rock
if player_choice == 0:
    print(f"You chose:\n{list_o_ascii[0]}")
    if computer_choice == 2:
        print(f"Computer chose:\n{list_o_ascii[2]}\nYou win!")
    elif computer_choice == 1:
        print(f"Computer chose:\n{list_o_ascii[1]}\nYou lose.")
    else:
        print(f"Computer chose:\n{list_o_ascii[0]}\nYou tie.")
# For paper
elif player_choice == 1:
    print(f"You chose:\n{list_o_ascii[player_choice]}")
    if computer_choice == 2:
        print(f"Computer chose:\n{list_o_ascii[2]}\nYou lose.")
    elif computer_choice == 0:
        print(f"Computer chose:\n{list_o_ascii[0]}\nYou win!")
    else:
        print(f"Computer chose:\n{list_o_ascii[1]}\nYou tie.")
# For scissors
elif player_choice == 2:
    print(f"You chose:\n{list_o_ascii[player_choice]}")
    if computer_choice == 0:
        print(f"Computer chose:\n{list_o_ascii[0]}\nYou lose.")
    elif computer_choice == 1:
        print(f"Computer chose:\n{list_o_ascii[1]}\nYou win!")
    else:
        print(f"Computer chose:\n{list_o_ascii[2]}\nYou tie.")
