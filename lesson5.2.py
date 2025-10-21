while True:
    num1, num2 = map(int, input("Enter two number: ").split())

    operation = input("Enter operation (*, /, +, -): ")


    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Error")
        else:
            print("Result:", num1 / num2)
    else:
        print("Error!")


    answer = input("You went continue?").lower()
    if answer not in ("y", "yes"):
        print("happy end.")
        break