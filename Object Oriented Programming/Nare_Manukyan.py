class BankAccount:

   def __init__(self, accountNumber, name, balance):
       self.accountNumber = accountNumber
       self.name = name
       self.balance = balance

   def Deposit(self, deposit):
       self.balance = self.balance + deposit

       return "User balance after {} deposit will be ".format(deposit) + str(self.balance)

   def  Withdraw(self, withdraw ):
       self.balance = self.balance - withdraw

       return "User balance after {} withdraw will be ".format(withdraw) +  str(self.balance)

   def bankFees(self):
       self.balance = (95/100) * self.balance

       print("Bank fees with a percentage of 5% of the balance account will be " + str(self.balance))

   def display(self):
       print("Customer account number is ", self.accountNumber)
       print("Customer name is ", self.name)
       print("Customer balance is ", self.balance)


customer = BankAccount(1564, "Airi Sato", 1000000)

print(customer.Deposit(int(input("Type deposit amount "))))
print(customer.Withdraw(int(input("Type withdraw amount "))))

customer.bankFees()
customer.display()



