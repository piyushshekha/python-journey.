name = input("Enter your name: ")
roll_number = int(input("Enter your roll number: "))
maths = float(input("Enter your maths marks: "))
science = float(input("Enter your science marks: "))
english = float(input("Enter your english marks: "))

total = maths + science + english
percentage = total / 3

print("\n----- STUDENT REPORT CARD -----")
print("Student Name   :", name)
print("Roll Number    :", roll_number)
print("Total Marks    :", total, "/ 300")
print("Percentage     :", percentage, "%")