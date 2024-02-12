# While loop
# Incrementing
number = 20
while number <= 25:
    print(number)
    number += 1

print("")

# Decrementing
num = 105
while num >= 100:
    print(num)
    num -= 1

# Break statement
print("")
a = 30
while a <= 40:
    print(a)
    if a == 36:
        break
    a += 1

# Continue
y = 29
while y < 35:
    y += 1
    if y == 32:
        continue
    print(y)

print("")

# For loop
languages = ["Python", "Java", "C++"]
for lang in languages:
    print(lang)

print("")

# Range
for mynumber in range(6):
    print(mynumber)

for mynum in range(20, 28):
    print(mynum)

for r in range(20, 30, 2):
    print(r)
