text = "Hello"
texttwo = "THERE"
textthree = " "
print(text)

# Accessing an element in string
print(text[1])

# Modifying a string
print(text.upper())
print(texttwo.lower())

# Size/Length of a string
print(len(text))

# String concatenation - Combining/Joining strings
print(text + textthree + texttwo)

# Assignment
# 1. Reassigning a value to a variable
new_text = text.replace("Hello", "Hii")
print(new_text)

# 2. Delete a variable
del text
print(text)

