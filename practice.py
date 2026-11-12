class car:
    driver_name = "asp nikhil"
    def __init__(self,name,model):
        self.name = name
        self.model = model
        print("adding a car for my garge")



s1 = car("BMW","M4")
print(s1.name, s1.model)

s2 = car("pagani","huraya")
print(s2.name, s2.model)

print(s2.driver_name)