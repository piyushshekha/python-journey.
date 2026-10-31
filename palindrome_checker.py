text1 = input("Enter a string: ")
text2 = text1.lower()

if text2 == text2[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")