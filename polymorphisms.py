# print(10 * 2)

# print([1, 2, 3, 4,5]*2)

# from random import *

# print(len("Hello"))
# print(len[1, 2, 3, "string"])
class Cat:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Cat name is : ", self.name)

c = Cat("Kitty")

class Dog:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Dog name is : ", self.name)

d = Dog("sheru")


def info(*a):
    for i in a:
        i.display()

info(c,d)