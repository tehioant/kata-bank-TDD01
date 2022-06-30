import datetime

import pandas as pd

from dataclasses import dataclass
from bank.exceptions import InsufficientBalanceError


@dataclass
class Transaction:
    Date: datetime.date
    Transaction: float
    Balance: float


class BankAccount:

    def __init__(self):
        self._balance = 0
        self._trading_operations_history = pd.DataFrame(columns=["Date", "Transaction", "Balance"])

    def get_balance(self) -> float:
        return self._balance

    def make_deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit value should be positive')
        self._balance += amount
        self.create_transaction(amount)

    def make_withdrawal(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal value should be positive')
        if self._balance < amount:
            raise InsufficientBalanceError(f"Insufficient funds : your current balance is {self._balance}")
        self._balance -= amount

    def get_trading_operation_history(self) -> pd.DataFrame:
        return self._trading_operations_history

    def create_transaction(self, amount):
        transaction = Transaction(datetime.date.today(), amount, self._balance)
        if self._trading_operations_history.empty:
            self._trading_operations_history = pd.DataFrame.from_dict(transaction.__dict__, orient='index').T
        else:
            self._trading_operations_history = pd.concat(
                [self._trading_operations_history, pd.DataFrame.from_dict(transaction.__dict__)])
