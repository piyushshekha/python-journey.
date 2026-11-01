secret_pin = (1234,)
account    = [5000,]

pin = int(input("Enter your pin "))

if pin ==secret_pin[0]:
    widrow = int(input("Enter your windrowal amount"))
    if widrow > account[0]:
        print("paise kam hain !")
    elif widrow % 100 != 0:
        print(" 100 ke note hi milenge")
    else:
        account[0] = account[0] - widrow
        print("bacha hua balnce",account[0])
else:
    print("galat pin")