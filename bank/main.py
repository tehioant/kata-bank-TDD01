from bank.exceptions import InsufficientBalanceError


class BankAccount:

    def __init__(self):
        self._balance = 0

    def get_balance(self) -> float:
        return self._balance

    def make_deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit value should be positive')
        self._balance += amount

    def make_withdrawal(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal value should be positive')
        if self._balance < amount:
            raise InsufficientBalanceError(f"Insufficient funds : your current balance is {self._balance}")
        self._balance -= amount
