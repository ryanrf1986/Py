class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def display_balance(self, amount):
        self.account_balance = amount
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
        return self, other_user


ryan = user('Ryan', 'ryanf@email.com')
ray = user('Ray', 'raymail@email.com')
aaron = user('aron', 'aaronmail@email.com')


ryan.make_deposit(500).make_deposit(500).make_deposit(500).make_withdraw(1149)
print(ryan.account_balance)
ray.make_deposit(500).make_deposit(500).make_withdraw(500).make_deposit(499)
print(ray.account_balance)
aaron.make_deposit(500).make_withdraw(100).make_withdraw(100).make_withdraw(299)
print(aaron.account_balance)


ryan.make_withdraw(500)
aaron.transfer_money(ryan, 500)
print('Aaron account balance', aaron.account_balance)
print('Ryan account balance', ryan.account_balance)