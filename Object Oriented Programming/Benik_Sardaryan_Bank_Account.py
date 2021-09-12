class BankAccount:
    def __init__(self, accountNumber, name, balance) -> None:
        self.accountNumber = int(accountNumber)
        self.name = name
        self.balance = int(balance)
        pass

    def Deposit(self, depo):
        self.balance = self.balance + depo
        pass

    def Withdrawal(self):
        print("Ваш баланс: $" + str(self.balance))
        self.withdr = int(input("Введите сумму, которую хотите вывести: " ))
        pass

    def bankFees(self):
        self.balance = self.balance * 0.95
        pass

    def Display(self):
        print("Номер аккаунта: " , self.accountNumber)
        print("Имя владельца: ", self.name)
        pass

    def Done(self):
        if self.withdr <= self.balance:
            print("Операция успешно завершена.")
            print("На балансе осталось: $" + str(self.balance - self.withdr))
        else:
            print("К сожалению на балансе нету столько ($" + str(self.withdr) + ") средств.")
            print("Максимум можно вывести: $" + str(self.balance))
            print("Попробуйте снова.")
        pass



acc = BankAccount(349873528123, "Python", 100)

acc.Display()
acc.Deposit(124)
acc.Withdrawal()
acc.Done()