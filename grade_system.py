percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:  # Automatically 90 se chota hai
    print("Grade: A")
elif percentage >= 70:  
    print("Grade: B")
elif percentage >= 60: 
    print("Grade: C")
else:
    print("Fail (Needs Improvement)")