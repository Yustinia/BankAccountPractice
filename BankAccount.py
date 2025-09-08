class BankAccount:
    def __init__(self, init_balance = 0):
        self.balance = init_balance

    def check_balance(self):
        print(f"Balance: '{self.balance}'")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.check_balance()
        elif amount == 0:
            print(f"Cannot deposit '{amount}' amount")
        else:
            print(f"Cannot deposit negative '{amount}' amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount == 0:
            print(f"Cannot withdraw '{amount}' amount")
        elif amount <= self.balance:
            self.balance -= amount
            self.check_balance()
