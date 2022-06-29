class BankAccount:

    def __init__(self):
        self._balance = 0

    def get_balance(self) -> float:
        return self._balance

    def make_deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit value should be positive')
        self._balance = amount
