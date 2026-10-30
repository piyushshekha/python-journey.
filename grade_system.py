percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:  # Automatically less than 90
    print("Grade: A")
elif percentage >= 70:  # Automatically less than 80
    print("Grade: B")
elif percentage >= 60:  # Automatically less than 70
    print("Grade: C")
else:
    print("Fail (Needs Improvement)")