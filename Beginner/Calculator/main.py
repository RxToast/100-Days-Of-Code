from art import calc_ascii

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operation_dict ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(f"{calc_ascii}\nWelcome to the Calculator!\n")
    number_1 = float(input("What is the first number?: "))

    should_retain = True

    while should_retain:
        for process in operation_dict:
            print(process)

        operation = input("Pick an operation: ")

        next_num = float(input("What is the next number?: "))

        answer = round(operation_dict[operation](number_1, next_num), 2)
        print(f"{number_1} {operation} {next_num} = {answer}")

        more = input(f"Type 'y' to continue working with {answer} or type 'n' to start a new calculation: ").lower()

        if more == "n":
            print("\n" * 20)
            calculator()
        elif more == "y":
            number_1 = answer

calculator()
