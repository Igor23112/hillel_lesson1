num1,num2 = map(int,input("enter 2 number").split())
operation = input("*, /, +, -")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Error: division by zero")
    else:
        print(int(num1 / num2))




