class Person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = Person("Shuntel", "17", "female")
accountant = Person("Myls", "18", "Male")
doctor = Person("Raymond", "28", "Male")
print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.firstname, accountant.age, accountant.gender)
print(doctor.firstname, doctor.age, doctor.gender)
teacher.details()

