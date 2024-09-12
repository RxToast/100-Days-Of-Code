print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Children's tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Enjoy your midlife crisis on us :)")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want your photo taken? Y or N: ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"your final bill is ${bill}")

else:
    print("You are not tall enough to ride this ride.")
