num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
op = input("enter operator (+, -, *, /, %, //):")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/" or op =="%" or op == "//":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        if op == "/":
            print(num1 / num2)
        elif op == "%":
            print(num1 % num2)
        elif op == "//":
            print(num1 // num2)
        else:
            print("Invalid operator entered!")