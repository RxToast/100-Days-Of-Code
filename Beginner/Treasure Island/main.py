print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroads = input("You are at a crossroads. Which way do you go?\n    Type Left or Right.\n")

if crossroads == "Left" or crossroads == "left":
    print("You arrive at a lake. There is an island in the middle of the lake.")

    swim_or_boat = input('    Type "Wait" to wait for a boat or type "Swim" to swim across.\n')
    if swim_or_boat == "Wait" or swim_or_boat == "wait":
        print("You arrive on the island unharmed where you see a castle with 3 doors. 1 Red, 1 Blue and 1 Yellow")

        door_picked = input('    Type "Red", "Blue" or "Yellow" to pick a door to enter\n')
        if door_picked == "Blue" or door_picked == "blue":
            print("You have found the treasure!")
        else:
            print("You were attacked by pirates. Game over.")

    else:
        print("You were eaten by sharks. Game over.")

else:
    print("You have fallen into a trap. Game over.")
