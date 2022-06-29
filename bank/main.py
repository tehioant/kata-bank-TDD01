class BankAccount:

    def __init__(self):
        self._balance = 0

    def get_balance(self) -> float:
        return self._balance

    def make_deposit(self, amount):
        self._balance = amount
