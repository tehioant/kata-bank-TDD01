import pytest as pytest
import pandas as pd

from bank.exceptions import InsufficientBalanceError
from bank.main import BankAccount


def test_given_bank_account_with_balance_zero_return_correct_balance():
    # GIVEN
    bank_account = BankAccount()

    # WHEN-THEN
    assert bank_account.get_balance() == 0


def test_access_private_variable_balance_impossible():
    # GIVEN

    # WHEN
    bank_account = BankAccount()

    # THEN
    with pytest.raises(AttributeError) as error:
        bank_account.balance == 0
    assert error.value.args[0] == "'BankAccount' object has no attribute 'balance'"


def test_given_bank_account_balance_when_make_two_deposits_should_return_balance():
    # GIVEN
    bank_account = BankAccount()

    # WHEN
    bank_account.make_deposit(1000)
    bank_account.make_deposit(650.5)

    # THEN
    assert bank_account.get_balance() == 1650.5


@pytest.mark.parametrize("deposit", [-2, 0])
def test_given_bank_account_balance_when_make_deposit_of_invalid_value_should_throw_exception(deposit):
    # GIVEN
    bank_account = BankAccount()
    # invalid_deposit_values = [-2, 0]

    # WHEN - THEN
    # for deposit_value in invalid_deposit_values:
    with pytest.raises(ValueError) as error:
        bank_account.make_deposit(deposit)
    assert error.value.args[0] == "Deposit value should be positive"


def test_given_bank_account_balance_when_make_withdrawal_should_return_correct_balance():
    # GIVEN
    bank_account = BankAccount()
    bank_account.make_deposit(1000)
    # WHEN
    bank_account.make_withdrawal(300)
    # THEN
    assert bank_account.get_balance() == 700


@pytest.mark.parametrize("deposit", [-10, 0])
def test_given_bank_account_balance_when_make_withdrawal_of_invalid_values_should_throw_an_exception(deposit):
    # GIVEN
    bank_account = BankAccount()

    # WHEN - THEN
    with pytest.raises(ValueError) as error:
        bank_account.make_withdrawal(deposit)
    assert error.value.args[0] == "Withdrawal value should be positive"


def test_given_bank_account_balance_with_150_when_make_withdrawal_of_200_should_throw_an_exception():
    # GIVEN
    bank_account = BankAccount()
    bank_account.make_deposit(150)
    # GIVEN
    # THEN
    with pytest.raises(InsufficientBalanceError) as error:
        bank_account.make_withdrawal(200)
    assert error.value.args[0] == f"Insufficient funds : your current balance is {bank_account.get_balance()}"


def test_given_deposit_150_should_return_trading_operation_history():
    # GIVEN
    bank_account = BankAccount()
    bank_account.make_deposit(150)
    # WHEN
    expected_trading_operation_history = pd.DataFrame(
        data={"Date": ["2022-06-29"], "Transaction": [150], "Balance": [150]})
    # THEN
    assert bank_account.get_trading_operation_history() == expected_trading_operation_history

# DONE open a bank account with amount at 0
# DONE obtain balance in bank account
# DONE make deposit of 10 recorded /with today's date
# DONE cannot make deposit <= 0
# DONE make withdrawal of 5 recorded /with today's date
# DONE cannot make withdrawal <= 0
# DONE handle exception when insufficient balance for withdrawal
# return list of all transactions sorted by date
