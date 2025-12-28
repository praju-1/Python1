class Pet:
    def __init__(self, pet_type, name, age):
        self.pet_type = pet_type
        self.name = name
        self.age = age

    def details(self):
        print("I am pet")

class Cat(Pet):
    def __init__(self, pet_type, name, age, bdate):
        super().__init__(pet_type, name, age)
        self.bdate = bdate

    def details(self):
        print("Bdate is  : ", self.bdate)
        print("pet type is  : ", self.pet_type)
        return super().details()
    

class Dog(Pet):
    def __init__(self, pet_type, name, age, breed):
        super().__init__(pet_type, name, age)
        self.breed = breed

    def details(self):
        print("breed is  : ", self.breed)
        print("pet type is  : ", self.pet_type)
        return super().details()
    
c = Cat("Cat", "Kitty", 2, 1)
c.details()

d = Dog("Dog", "sheru", 1, "German")
d.details()