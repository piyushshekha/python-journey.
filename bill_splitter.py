total_bill = float(input("Enter your total bill :"))
total_friends = int(input("Enter your total friends:"))
tip_per = float(input( "Enetr your tip :"))

tip_amount = total_bill * (tip_per/100)
grand_total = total_bill + tip_amount
per_person_pay = grand_total / total_friends

print(f"total bill with tip: {grand_total} | Each friend pays : {per_person_pay}")