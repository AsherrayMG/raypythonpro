try:
    print(x)
except:
    print("Name error occurred")
finally:
    print("Success")

try:
    num1 = 20
    num2 = 0

    print(num1 / num2)
except:
    print("Zero division error occurred")
finally:
    print("Success")

# User defined function
try:
    def sum(first, second):
        return first + second
except:
    print("Exception occurred")


print(sum(10, 20))
