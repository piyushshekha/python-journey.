def get_discount(amount):
    if amount >= 1000:
        return 200
    elif amount >= 500:
        return 50
    else:
        return 0
    
bills = [1200,400,850,2000,300]

for amount in bills:
    pay = get_discount(amount)
    final = amount - pay
    print(f"bills amount:{amount:<9} |discount :{pay:<8} |final payable :{final:<10}")
      