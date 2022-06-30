import datetime
import uuid
from dataclasses import dataclass

import pandas as pd

from bank.exceptions import InsufficientBalanceError
from bank.time import TimeService


@dataclass
class Transaction:
    Date: datetime.date
    Transaction: float
    Balance: float


class Bank:

    def __init__(self):
        self._accounts = {}

    def get_accounts(self) -> dict:
        return self._accounts

    def create_account(self) -> uuid.UUID:
        iban = uuid.uuid4()
        self._accounts.update({iban: BankAccount(iban)})
        return iban

    def get_account_by_iban(self, iban):
        try:
            return self._accounts[iban]
        except KeyError:
            raise KeyError("iban not found in accounts")

    def transfer(self, iban_from, iban_to, amount):
        pass


# def transfer(iban_from, iban_to, amount):


class BankAccount:

    def __init__(self, iban):
        self._iban = iban
        self._balance = 0
        self._trading_operations_history = pd.DataFrame(columns=["Date", "Transaction", "Balance"])

    def get_iban(self):
        return self._iban

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
        self.create_transaction(-amount)

    def get_trading_operation_history(self) -> pd.DataFrame:
        return self._trading_operations_history.sort_values("Date", ascending=False).reset_index(drop=True)

    def create_transaction(self, amount):
        transaction = Transaction(TimeService.get_time_now(), amount, self._balance)
        list_transactions = self._trading_operations_history.to_dict(orient="records")
        list_transactions.append(transaction.__dict__)
        self._trading_operations_history = pd.DataFrame(list_transactions)
