class BankAccount:

    def __init__(self):
        self.balance = 0

    def get_balance(self) -> float:
        return self.balance

    def make_deposit(self, amount):
        self.balance = amount
