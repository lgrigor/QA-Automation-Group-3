class BankAccount:
    
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance 

    def deposit(self):
        self.balance = self.balance + int(input("Enter the amount: "))
        return self.balance

    def withdrawal(self):
        amount = int(input("Enter the amount: "))
        if self.balance < amount:
            print("No sufficient balance")
        else:
            self.balance = self.balance - amount
        return self.balance

    def bankfees(self):
        self.balance = self.balance * 0.95
        return self.balance

    def display(self):
        return {
            "accountNumber":self.accountNumber,
            "name":self.name,
            "balance":self.balance
        }

user1 = BankAccount(12459632, "Lyudmila Barseghyan", 200000)

print(user1.deposit())
print(user1.withdrawal())
print(user1.display())