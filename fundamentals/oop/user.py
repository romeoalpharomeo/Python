"""
If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

For this assignment, we'll add some functionality to the User class:

make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
"""
class User():
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: " + str(self.account_balance))
        return self
    def transfer_money(self, account_receiving, amount_to_transfer):
        self.make_withdrawal(amount_to_transfer)
        account_receiving.account_balance += amount_to_transfer
        return self

tori = User("Victoria")
tom = User("Thomas")
sally = User("Sally")

tori.make_deposit(10000).make_deposit(10000).make_deposit(10000).make_withdrawal(1000).display_user_balance().transfer_money(tom, 1000).display_user_balance()
tom.make_deposit(500).make_deposit(1500).make_withdrawal(500).display_user_balance().transfer_money(sally, 1000).display_user_balance()
sally.make_deposit(1000).make_withdrawal(50).display_user_balance()
