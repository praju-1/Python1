from abc import ABC, abstractmethod

class Vehical(ABC):
    def __init__(self, brand, model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def get_details(self):
        return f"{self.brand}{self.model}- Fuel Type : {self.fuel_type}"
    
# v = Vehical("toyota","xuv", "Petrol")
# concrete class

class Car(Vehical):
    def start_engine(self):
        print(f"The {self.brand}{self.model} Car's engine has started")
    
    def stop_engine(self):
        print(f"The {self.brand}{self.model} Car's engine has stopped")

c = Car("toyota","xuv", "Petrol")
print(c.get_details())
c.start_engine()