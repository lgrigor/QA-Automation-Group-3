class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def Deposit(self , deposit):
        self.balance = self.balance + deposit
    
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w

    def bankFees(self):
        self.balance = (95/100)*self.balance

    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        

newAccount = BankAccount(2178514584, "Albert" , 2700)

newAccount.Withdrawal(300)

newAccount.Deposit(200)

newAccount.display()
