# Area of a triangle - 1/2 * (height * base)
height = int(input("Enter height:"))
base = int(input("Enter base:"))

area = 1 / 2 * (height * base)
print("Area:", 1 / 2 * (height * base))

p = float(input("Enter first number:"))
q = float(input("Enter second number:"))
operator = input("Enter operator:")
if operator == "+":
    print("The result is:", p + q)
elif operator == "-":
    print("The result is:", p - q)
elif operator == "*":
    print("The result is:", p * q)
elif operator == "/":
    print("The result is:", p / q)
else:
    print("Invalid")
