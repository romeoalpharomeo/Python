class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("Guido", "guido@dojo.com")
tammy = User("Tammy", "tammy@tamtam.com")

tammy.make_deposit(10000)
print(tammy.account_balance)
print(tammy.email)

