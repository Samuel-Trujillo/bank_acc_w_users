class BankAccount:
    bank_name= "Bank of Sam"
    def __init__(self, account_name ="checking", int_rate= .20, cash= 0):
        self.account_name= account_name
        self.int_rate = int_rate
        self.cash= cash
    def deposit(self, dep):
        self.cash += dep
        return self
    def withdraw(self, wdraw):
        self.cash -= wdraw
        return self
    def display_account(self):
        self.display_account= print(f"{self.bank_name}, Account: {self.account_name}, Balance of: {self.cash}")
        return self
    def add_interest(self):
        if self.cash >0:
            self.cash = self.cash + (self.int_rate * self.cash)
        else:
            print("YOU ARE BROKE")
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
    def deposit(self,dep):
        self.account.deposit(dep)
        return self
    def withdraw(self, wdraw):
        self.account.withdraw(wdraw)
        return self
    def balance(self):
        print(f"{self.account.display_account()}")
        return self
    def add_interest(self):
        self.account.add_interest()
        return self

sam= User("Sam")
sam.deposit(0)
sam.withdraw(0)
sam.add_interest()
sam.balance()
