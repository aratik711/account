class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        self.commit()

    def deposit(self, amount):
        self.balance += amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    """This class generates checking account object"""

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= (amount+self.fee)
        Account.commit(self)


jacks_checking = Checking("jacks_balance.txt", 5)
jacks_checking.deposit(100)
print(jacks_checking.balance)
jacks_checking.transfer(110)
print(jacks_checking.type + " " + str(jacks_checking.balance))

johns_checking = Checking("johns_balance.txt", 5)
johns_checking.deposit(100)
print(johns_checking.balance)
johns_checking.transfer(110)
print(johns_checking.type + " " + str(johns_checking.balance))

print(johns_checking.__doc__)

"""account=Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(400)
print(account.balance)"""