def calculate(num1, num2, opration):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "invalid operation"
    
num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
operation = input("input operation: ")

result = calculate(num1, num2, operation)

print(f"The result of {num1} {operation} {num2} is: {result}")






     