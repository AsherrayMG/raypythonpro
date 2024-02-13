# A class is a blueprint of an object
# An object is an instance of a class


class Person:
    # Properties/Attributes/Characteristics
    name = "Joe"
    age = 24

    # Method/Function/behaviour
    def talk(self):
        print("Person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)
