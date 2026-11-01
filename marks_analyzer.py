list1 = [66,50,98,54,66,]
list1.sort()

lowest = list1[0]
highest = list1[-1]

print("lowest marks is:",lowest)
print("highest marks is:",highest)

diff = highest - lowest
print ("difference is",diff)
if lowest < 50:
    print("Warning: At least one student needs improvement!")
else:
    print("Good job: All students scored above 50!")

