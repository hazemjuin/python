class BankAccount:
    accounts = []

    def __init__(self, interest_rate=0, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            print(f"Interest Rate: {account.interest_rate}, Balance: {account.balance}")

# Create two accounts
account1 = BankAccount(0.05, 1000)
account2 = BankAccount(0.1, 500)

# Chain operations on the first account
account1.deposit(200).deposit(300).deposit(500).withdraw(400).yield_interest().display_account_info()

# Chain operations on the second account
account2.deposit(100).deposit(50).withdraw(75).withdraw(100).withdraw(50).withdraw(200).yield_interest().display_account_info()

# Print all accounts' information
BankAccount.print_all_accounts_info()
