# def function_name(parameters):
#     exce
# function_name(arguments)


# class classname:
#     exectution

# c = classname()
# c.

# class msg:
#     def hello(self):
#         print("Hello world")
    
#     def test(self, a, b):
#         print(a+b)

# m = msg()
# m.hello()
# m.test(10, 20)

class Calculator:
    def __init__(self, a, b=20):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def div(self):
        print(self.a / self.b)

    def mult(self):
        print(self.a * self.b)

c = Calculator(10, 20)
c.add()
c.div()