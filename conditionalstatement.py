temperature = 34

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that determines the largest number among three numbers
num1 = 78
num2 = 90
num3 = 23
if num1 > num2 and num1 > num3:
    print(num1, "is largest number")

elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")

else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 45

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is prime or not
num = 19
if num > 1:
    for p in range(2, num):
        if num % p == 0:
            print("Not prime number")
        else:
            print("The number is prime")
            break

    else:
        print("Not prime number")

