class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposite(self, amount):
        self.balance = self.balance + amount

    def widthdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient Fund")

    def print_balance(self):
        return self.balance


account = BankAccount()

print(account.print_balance())

account.deposite(100)

print(account.print_balance())

account.widthdraw(50)

print(account.print_balance())

account.deposite(500)

print(account.print_balance())


account.widthdraw(1000)

account.print_balance()