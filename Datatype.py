# Data type
number = 67  # int
num = 78.98  # float
greetings = "Hello there"  # str
IsPythonInteresting = True  # bool

# A variable storing multiple values
language = ["Python", "JavaScript", "PHP"]  # list
fruits = ("apple", "banana", "orange", "pear")  # Tuple
countries = {"Russia", "Porland", "France"}  # Set
# Dictionary
details = {
    "FirstName": "Brian",
    "age": 17,
    "course": "MIT",
    "nationality": "Kenya"

}
print(details["course"])
print(number)
print(IsPythonInteresting)
print(countries)
print(details)

# Determining the data type
print(type(details))
print(type(countries))
print(type(language))

# Typecasting - Converting one data type to another
print(float(number))
print(int(num))
