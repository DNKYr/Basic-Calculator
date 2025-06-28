try: 
    first_number = int(input("Please input the first number \n"))
    operation_type = str(input("Now please input the operation you want to perform (eg. +, -, *, /)\n"))
    second_number = int(input("Please input the second number\n"))

    if operation_type == "+":
        print(first_number + second_number)
    elif operation_type == "-":
        print(first_number - second_number)
    elif operation_type == "*":
        print(first_number * second_number)
    elif operation_type == '/':
        print(first_number / second_number)
    else:
        print("This is an invalid operation. Please restart the program")
except ZeroDivisionError as e:
    print(f"ZeroDvisionError: Division by Zero is undefined")
except ValueError as e:
    print(f"ValueError: Please input a number in its numeral format (eg. 10, 20, 34, 1)")
