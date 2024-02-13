# Parent class/Super class/

class Animal:
    def sound(self):
        print("Animal is speaking")


# Child class/Subclass/Derived class

class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


a = Animal()

d = Dog()
d.bark()

c = Cat()
c.meow()
