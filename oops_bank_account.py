class Account: 
      
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
        

    def debit(self,amount):
        self.balance -= amount
        print(f"{amount} debited. balance: {self.balance}")
    
    def credit(self,amount):
        self.balance += amount
        print(f"{amount}credited. balance:{self.balance}")
    
    

acc1 = Account("ACC123", 10000)
acc1.debit(2000) 
acc1.credit(5000)