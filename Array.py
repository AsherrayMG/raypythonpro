courses = ["MIT", "Cyber Sec", "Data science"]

print(courses)
# Accessing an element in an array
print(courses[1])

# Looping through an array
for course in courses:
    print(course)

# Adding a new element in an array
courses.append("Android Programming")
print(courses)

# Deleting an element from an array
courses.remove("Cyber Sec")
print(courses)
