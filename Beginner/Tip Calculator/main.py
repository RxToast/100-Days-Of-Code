print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))

tip_percent = float(input("How much would you like to tip? 10, 12, or 15? "))

tip = bill / 100 * tip_percent

num_people = float(input("How many people will split the bill? "))

each_pay = round((bill + tip) / num_people, 2)

print(f"Each person should pay: {each_pay}")
