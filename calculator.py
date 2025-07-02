import sys

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num1 == 0 or num2 == 0:
        result = "Error: Division by Zero"
    else:
        result = num1 / num2
else:
    result = "Invalid Operator"

print(result)
