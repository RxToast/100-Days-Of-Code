from art import calc_start_art

print(calc_start_art)

num_to_do = float(input("What's the first number?: "))
num_2_do = float(input("What's the next number?: "))
operation = input("+\n-\n*\n/\nPick an operation: ")

calc_on = True

answer = 0

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

def do_calc(num1, num2):
    global answer

    if operation == "+":
        answer = round(addition(num1, num2), 2)
        print(f"{num1} + {num2} = {answer}")
    elif operation == "-":
        answer = round(subtraction(num1, num2), 2)
        print(f"{num1} - {num2} = {answer}")
    elif operation == "*":
        answer = round(multiplication(num1, num2), 2)
        print(f"{num1} * {num2} = {answer}")
    elif operation == "/":
        answer = round(division(num1, num2), 2)
        print(f"{num1} / {num2} = {answer}")
    else:
        print("Invalid operation")

def another_calc(num1, num2):
    do_calc(num1=num1, num2=num2)

do_calc(num_to_do, num_2_do)

while calc_on:

    do_more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    if do_more == "y":
        operation = input("+\n-\n*\n/\nPick an operation: ")
        num_3_do = float(input("What's the next number?: "))
        another_calc(num1=answer, num2=num_3_do)
    elif do_more == "n":
        pass
