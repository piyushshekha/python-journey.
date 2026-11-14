class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def avg_cal(self):
        total = 0
        for val in self.marks: 
            total += val
        print(self.name,"your avreg is :",total/len(self.marks))
            
s1 = Student("piyush", [79,87,99]) 
s1.avg_cal()

class Complax:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def show_no(self):
       print(self.real,"i +",self.img,"j")
       
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complax(newreal,newimg)
    
    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complax(newreal,newimg)

num1 = Complax(10,6)
num1.show_no()

num2 = Complax(3,5)
num2.show_no()

num3 = num1 - num2
num3.show_no()


class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showdetail(self):
        print("role",self.role)
        print("dept",self.dept)
        print("salary",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Enginner","it","75,000")
        

eng1 = Engineer("nikhil",60)
eng1.showdetail()
        
        
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("chips",50)
order2 = Order("chips",30)

print(order1 > order2)