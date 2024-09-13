from ascii import list_o_ascii
import random

player_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice <0:
    print("Invalid entry, you lose.")
elif player_choice == 0 and computer_choice == 2:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou win!")
elif computer_choice > player_choice:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou lose.")
elif player_choice == computer_choice:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou tie.")
elif computer_choice == 0 and player_choice == 2:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou lose.")
elif player_choice > computer_choice:
    print(f"You chose:\n{list_o_ascii[player_choice]}\nComputer chose:\n{list_o_ascii[computer_choice]}\nYou win!")
