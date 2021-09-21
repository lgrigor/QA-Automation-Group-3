class BankAccount:
  def __init__(self, accountNumber, name, balance):
    self.accountNumber = accountNumber
    self.name = name
    self.balance = balance

  def deposit(self):
    balance1 = float(input('Enter your deposit: '))
    self.balance += balance1
    print('Your balance after deposit is:')
    print(self.balance)

  def withdrawal(self):
    balance2 = float(input('Enter your withdrawal: '))
    if balance2 < self.balance:
      self.balance -= balance2
      print('Your balance after withdrawal is:')
      print(self.balance)
    else:
      print("You don't have enough money")

  def bankFees(self):
    balance3 = 0.95*(self.balance)
    self.balance -= balance3
    print('Your bankFee is:')
    print(self.balance)
    print('Your balance after bankFee is: ', + balance3)
    self.balance = balance3

  def display(self):
    print('Information about card holder:')
    print(self.accountNumber, self.name, self.balance)


bankAccount = BankAccount("accountNumber is: 1021401,", "cardHolderName: Aram,", 0)
bankAccount.deposit()
bankAccount.withdrawal()
bankAccount.bankFees()
bankAccount.display()
