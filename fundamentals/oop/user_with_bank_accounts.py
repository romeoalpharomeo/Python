"""
If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

For this assignment, we'll add some functionality to the User class:

make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
"""
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



class User():
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print("User: " + self.name)
        self.account.display_account_info()
        return self
    def transfer_money(self, account_receiving, amount_to_transfer):
        self.account.withdraw(amount_to_transfer)
        account_receiving.account.deposit(amount_to_transfer)
        return self

tori = User("Victoria")
tom = User("Thomas")
sally = User("Sally")

tori.make_deposit(10000).make_deposit(10000).make_deposit(10000).make_withdrawal(1000).display_user_balance().transfer_money(tom, 1000).display_user_balance()
tom.make_deposit(500).make_deposit(1500).make_withdrawal(500).display_user_balance().transfer_money(sally, 1000).display_user_balance()
sally.make_deposit(1000).make_withdrawal(50).display_user_balance()
