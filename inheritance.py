class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name of emp is : ", self.name)
        print('Age of emp is : ', self.age)

# e = Employee("John", 21)
# e.info()

class Trainer(Employee):
    def __init__(self, name,age, role):
        Employee.__init__(self, name,age)
        self.role = role

    def info(self):
        # Employee.info(self)
        print("Job role is :", self.role)
        return super().info()
    

class Manager(Trainer):
    def __init__(self, name, age,role, salary):
        super().__init__(name,age, role)
        self.salary = salary

    def info(self):
        print("Salary is  : ", self.salary)
        return super().info()



m = Manager("adf", 21, "trainer", 23324)
m.info()
