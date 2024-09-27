MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_values = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

amt_quarters = 0
amt_dimes = 0
amt_nickels = 0
amt_pennies = 0

money_in_machine = 0.00

def insert_money():
    global amt_quarters, amt_dimes, amt_nickels, amt_pennies, money_in_machine
    money_in = 0.00

    print("Please insert coins.")

    amt_quarters = int(input("How many quarters?: "))
    money_in += amt_quarters * coin_values["quarter"]

    amt_dimes = int(input("How many dimes?: "))
    money_in += amt_dimes * coin_values["dime"]

    amt_nickels = int(input("How many nickels?: "))
    money_in += amt_nickels * coin_values["nickel"]

    amt_pennies = int(input("How many pennies?: "))
    money_in += amt_pennies * coin_values["penny"]

    money_in_machine += money_in

    return money_in

def check_resources(drink):
     for ingredient in MENU[f"{drink}"]["ingredients"]:
        if MENU[f"{drink}"]["ingredients"][f"{ingredient}"] > resources[f"{ingredient}"]:
            print("\nNot enough ingredients for drink. Try another selection or come back later! :)\n")
            run_machine()

def check_money(drink, money):
    global money_in_machine
    if MENU[f"{drink}"]["cost"] > money:
        print("\nNot enough money inserted. You have been refunded. Please make another selection or try again.\n")
        print(f"Refunded: {money}")
        print(f"{amt_quarters} Quarters\n{amt_dimes} Dimes\n{amt_nickels} Nickels\n{amt_pennies} Pennies\n")
        money_in_machine -= money
        run_machine()
    elif MENU[f"{drink}"]["cost"] < money:
        print(f"\nYour change is ${round(money - MENU[f"{drink}"]["cost"], 2)}")
        money_in_machine -= money - MENU[f"{drink}"]["cost"]
    else:
        print("\nYou put in the exact amount of money, your change is: $0.00")

def subtract_ingredients(drink):
    for resource in resources:
        if drink == "latte" and resource == "milk":
            continue
        resources[resource] -= MENU[drink]["ingredients"].get(resource, 0)

def run_machine():

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        return
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        print(f"Money: {round(money_in_machine, 2)}")
        run_machine()
    elif choice == "espresso":
        check_resources(drink=choice)
        money_inserted = insert_money()
        check_money(drink=choice, money=money_inserted)
        subtract_ingredients(drink=choice)
        print(f"\nHere's your {choice.capitalize()}. Enjoy.")
        run_machine()

    elif choice == "latte":
        check_resources(drink=choice)
        money_inserted = insert_money()
        check_money(drink=choice, money=money_inserted)
        subtract_ingredients(drink=choice)
        print(f"\nHere's your {choice.capitalize()}. Enjoy.")
        run_machine()

    elif choice == "cappuccino":
        check_resources(drink=choice)
        money_inserted = insert_money()
        check_money(drink=choice, money=money_inserted)
        subtract_ingredients(drink=choice)
        print(f"\nHere's your {choice.capitalize()}. Enjoy.\n")
        run_machine()
    else:
        print("Invalid input. Try again.")
        run_machine()

run_machine()
