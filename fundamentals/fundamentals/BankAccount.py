class BankAccount:
    population = 0
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.population += 1
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdrawl(self, amount):
        if self.balance > amount:
            self.balance -= 0 
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        self.display_account_info
        print(f'{self.balance}')
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += self.int_rate
        return self
        # your code here
    @classmethod
    def user_population(cls):
        print(f'Number of Bank Accounts: {cls.population}')

act1 = BankAccount(.04, 250)
act2 = BankAccount(.07, 1100)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
act1.deposit(500).deposit(400).deposit(300).withdrawl(700).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
act2.deposit(500).deposit(500).withdrawl(250).withdrawl(250).withdrawl(100).withdrawl(100).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.user_population()
