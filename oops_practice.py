class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
        print("adding a car for my garge")
    def hello(self):
        print("nikhil dirve the ",self.name)
    
    def mod_det(self):
        return self.model
    
s1 = Car("BMW","M4")
print(s1.name, s1.model)
s1.hello()
print("model no :",s1.mod_det())
    
class ElectricCar(Car):
    def charge(self):
        print(f"{self.name} is charging its battery!")
        super().hello()
        
ev1 = ElectricCar("Tesla", "Model S")
ev1.hello()   
ev1.charge() 


