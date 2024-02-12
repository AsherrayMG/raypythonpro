# Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

y = min(34, 78, 90, 123, 45)
print(y)

d = pow(2, 3)
print(d)


# User defined function
def name():
    print("Teddy")


name()  # Coding a function


def details():
    Name = ("Frank")
    Age = 15
    course = "MIT"
    print(Name, Age, course)


details()


# Parameters/variables and arguments/values
def patient(name, gender, age, MarriageStatus):
    print(name, gender, age, MarriageStatus)


patient("Frank", "male", "15", "Single")
patient("Gabriel", "female", "19", "Single")


def multiply(a, b):
    print(a * b)


print("")

multiply(15, 15)
multiply(25, 25)
multiply(35, 35)


# Create a user-defined function
# called employees Display details
def employees(Fullname, age, position, salary):
    print(Fullname, age, position, salary)


employees("Frank Kinoti", "35", "Manager", "120,000")
employees("Mary Wanjala", "30", "P.A", "100,000")
employees("Wilfred  Nyaga", "27", "Secretary", "96,000")
employees("Benson Muthomi", "36", "Treasurer", "50,000")
employees("Ann Nafula", "37", "Cleaner", "6,000")

employees()
