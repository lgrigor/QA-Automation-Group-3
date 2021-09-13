class BankAccount:
   def __init__(self, accountNumber, name, balance):
       self.accountNumber = accountNumber
       self.name = name
       self.balance = balance

   def deposit(self, deposit):
       self.balance += deposit


   def withdrawal(self, withdrawal):
       if withdrawal < self.balance:
   		self.balance -= withdrawal
   else:
   		print("You don't have enough money on your balance sheet")


   def bankFees(self, fee = 5):
       balanceFee = self.balance * (fee / 100)
       self.balance -= balanceFee


   def display(self):
       print("BankAccount is " + str(self.accountNumber) + 
	          "\n" + "Account name is " + str(self.name) + 
			  "\n" + "balanc is  " + str(self.balance))


mybankAccount = BankAccount(1, "Gevorg", 20000)
print(mybankAccount.display())
