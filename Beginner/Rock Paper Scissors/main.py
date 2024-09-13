from ascii import list_o_ascii
import random

player_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if player_choice == 0 and computer_choice == 2:
    print(f"You chose:\n{list_o_ascii[0]}\nComputer chose:\n{list_o_ascii[2]}\nYou win!")
elif computer_choice > player_choice:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou lose.")
    