'''Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (integer type), name (name of the account owner as string type), balance(integer type).
Create a constructor with parameters: accountNumber, name, balance.

1. Create a Deposit() method which manages the deposit actions.
2. Create a Withdrawal() method which manages withdrawals actions.
3. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
4. Create a display() method to display account details (accountNumber, name, balance).

Create an instance and check if everything is working correctly.
'''
class Bank_Account:
    
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self):
        amount = float(input("Enter deposit amount:"))
        self.balance += amount
        print("Your deposit amount is:",self.balance)
        

    def Withdrawal(self):
        amount = float(input("Enter withdrawl amount:"))
        if amount > self.balance:
          print("You have no enough money")
        else:
          self.balance = self.balance - amount
          print("Your withdrawl is:", self.balance)
        

    def bankFees(self):
        print(self.balance)
        self.balance = (95/100)*self.balance
        print('The result is:',self.balance)

    def display(self):
        print("accountNumber:", self.accountNumber)
        print("Name:", self.name)
        print("Balance:", self. balance, "$")


x = Bank_Account(123156, 'Helena', 11)
x.Deposit()

y = Bank_Account(54654,"EDEWDW", 5)
y.Withdrawal()

z=Bank_Account(3555,"Helena", 5896)
z.bankFees()

g = Bank_Account(1234, "Helena", "" )
g.display()
