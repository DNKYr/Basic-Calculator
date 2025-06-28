import operator
operation_dict = {
    "+": operator.add,
    "add": operator.add,
    "-": operator.sub,
    "minus": operator.sub,
    "*": operator.mul,
    "multiply": operator.mul,
    "/": operator.truediv,
    "divide": operator.truediv
}
def calculate(first_number, second_number, operation_type):
    ops = operation_dict.get(operation_type)
    if ops is None:
        raise ValueError(f"{operation_type} is an invalid operatoin")
    return ops(first_number, second_number)

def print_welcome_message():
    print("Welcome to basic calculator. This calculator takes commmand line input and output the result in command line too. \n Step to use it: \n 1. Input the first number (in numerical format) \n 2. Input the operation you want to perform (eg. +, -, *, /) \n 3. Input the second number (in numerical format)")

def print_outro_message():
    print("Thank you for using basic calculator. ")
repeat = True
print_welcome_message()
while repeat:
    try: 
        first_number = int(input("Please input the first number \n"))
        operation_type = str(input("Now please input the operation you want to perform (eg. +, -, *, /)\n"))
        second_number = int(input("Please input the second number\n"))

        result = calculate(first_number, second_number, operation_type)
        print(result)
    except ZeroDivisionError as e:
        print(f"ZeroDvisionError: Division by Zero is undefined")
    except ValueError as e:
        print(f"ValueError: {e}")
    
    r = str(input("Do you want to end this program? If yes please enter: STOP \n"))
    if r == "STOP":
        repeat = False

print_outro_message()