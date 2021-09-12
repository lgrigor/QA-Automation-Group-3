class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    # create Deposit() method
    def Deposit(self , d):
        self.balance = self.balance + d
    
    # create Withdrawal method
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
            
    # create bankFees() method
    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    # create display() method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        
# Testing the code :
newAccount = BankAccount(2178514584, "Albert" , 2700)

# Creating Withdrawal Test
newAccount.Withdrawal(300)

# Create deposit test
newAccount.Deposit(200)

# Display account informations
newAccount.display()
