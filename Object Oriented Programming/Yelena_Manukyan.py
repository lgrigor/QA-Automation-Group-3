class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance 

    def Deposit (self, sum):
        self.balance += sum  

    def Withdrawal (self, sum):
        if sum <= self.balance:
           self.balance -= sum
        
    def bankFees (self, sum):
         if self.balance > 0:
            self.balance-=self.balance % 95
    


Yelena = BankAccount (1111, "Yelena", 2222)
Yelena.Deposit(3333)
print (Yelena.balance)

Yelena.Withdrawal(11)
print (Yelena.balance)

Yelena.bankFees(Yelena.balance % 95)
print(Yelena.balance)

print(Yelena.accountNumber,Yelena. name, Yelena.balance)