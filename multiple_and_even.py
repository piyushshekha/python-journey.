num = int(input("Enter a number: "))

if num % 2 ==0 and num % 7 == 0:
    print("is even and is multiple of 7")
elif num % 7 == 0 and num % 2 != 0:
    print("is odd and is multiple of 7")
elif num % 2 == 0 and num % 7 != 0:
    print("is even and is not multiple of 7")
else:
    print("is not even and is not multiple of 7")