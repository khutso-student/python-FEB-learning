get1 = float(input("Enter the first number: "))
get2 = float(input("Enter the second number: "))
active = input("Enter an operation (+, -, *, /): ")


if active == "+":
    result = get1 + get2
    print(f"{get1} + {get2} = {result}")
elif active == "-":
    result = get1 - get2
    print(f"{get1} - {get2} = {result}")
elif active == "*":
    result = get1 * get2
    print(f"{get1} * {get2} = {result}")
elif active == "/":
    if get2 != 0:  # Prevent division by zero
        result = get1 / get2
        print(f"{get1} / {get2} = {result}")
    else:
        print("Error zero is not allowed.")
else:
    print("Invalid . Please enter +, -, *, or /.")