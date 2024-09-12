weight = float(input("What is your weight in kilos? "))
height = float(input("What is your height in meters? "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi <24.9:
    print("normal weight")
else:
    print("overweight")