a = int(input("Enter a: "))
b = int(input("Enter b: "))    
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Greatest number is:", a)
elif b >= c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)