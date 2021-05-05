class BankAccount():
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = 0
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.int_rate*self.balance)
        return self
    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self
    
account_one = BankAccount()
account_one.int_rate = .3
account_one.deposit(50).deposit(100).deposit(50).withdraw(100).yield_interest().display_account_info()

account_two = BankAccount()
account_two.int_rate = .12
account_two.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()


