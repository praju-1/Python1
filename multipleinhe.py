class Father:
    def __init__(self, eyes, hair):
        self.eyes = eyes
        self.hair =  hair

    def info(self):
        print("Eyes of father is  : ", self.eyes)
        print("Hair style is : ", self.hair)


class Mother:
    def __init__(self, height):
        self.height = height

    def info(self):
        print("Height is : ", self.height)


class Son(Father, Mother):
    def __init__(self, eyes, hair, height, name):
        Father.__init__(self, eyes, hair)
        Mother.__init__(self, height)
        # super().__init__(eyes, hair)
        # super().__init__(height)
        self.name = name

    def info(self):
        Father.info(self)
        Mother.info(self)
        print("Name is : ", self.name)


s = Son("Brown", "Curly", "Tall", "john")
print(s)