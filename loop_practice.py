n = int(input("enter your for table :"))
i = 1

while i <= 10 :
    print(n*i)
    i += 1
    
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0

for val in nums:
    if val == x:
        print("found",x ,"at index : ",i)
        break
    i += 1
    
