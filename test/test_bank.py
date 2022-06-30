import datetime
import uuid
from unittest import TestCase
from unittest.mock import patch

import pandas as pd
import pytest as pytest

from bank.exceptions import InsufficientBalanceError
from bank.main import BankAccount, Bank
from bank.time import TimeService


def test_when_create_bank_account_should_have_balance_zero_and_empty_operation_history():
    # GIVEN
    iban = uuid.uuid4()
    bank_account = BankAccount(iban)

    # WHEN-THEN
    assert bank_account.get_iban() == iban
    assert bank_account.get_balance() == 0
    assert bank_account.get_trading_operation_history().empty


def test_access_private_variable_balance_impossible():
    # GIVEN

    # WHEN
    bank_account = BankAccount(uuid.uuid4())

    # THEN
    with pytest.raises(AttributeError) as error:
        bank_account.balance == 0
    assert error.value.args[0] == "'BankAccount' object has no attribute 'balance'"


def test_given_bank_account_balance_when_make_two_deposits_should_return_balance():
    # GIVEN
    bank_account = BankAccount(uuid.uuid4())

    # WHEN
    bank_account.make_deposit(1000)
    bank_account.make_deposit(650.5)

    # THEN
    assert bank_account.get_balance() == 1650.5


@pytest.mark.parametrize("deposit", [-2, 0])
def test_given_bank_account_balance_when_make_deposit_of_invalid_value_should_throw_exception(deposit):
    # GIVEN
    bank_account = BankAccount(uuid.uuid4())
    # invalid_deposit_values = [-2, 0]

    # WHEN - THEN
    # for deposit_value in invalid_deposit_values:
    with pytest.raises(ValueError) as error:
        bank_account.make_deposit(deposit)
    assert error.value.args[0] == "Deposit value should be positive"
    assert bank_account.get_trading_operation_history().empty


def test_given_bank_account_balance_when_make_withdrawal_should_return_correct_balance():
    # GIVEN
    bank_account = BankAccount(uuid.uuid4())
    bank_account.make_deposit(1000)
    # WHEN
    bank_account.make_withdrawal(300)
    # THEN
    assert bank_account.get_balance() == 700


@pytest.mark.parametrize("deposit", [-10, 0])
def test_given_bank_account_balance_when_make_withdrawal_of_invalid_values_should_throw_an_exception(deposit):
    # GIVEN
    bank_account = BankAccount(uuid.uuid4())

    # WHEN - THEN
    with pytest.raises(ValueError) as error:
        bank_account.make_withdrawal(deposit)
    assert error.value.args[0] == "Withdrawal value should be positive"
    assert bank_account.get_trading_operation_history().empty


def test_given_bank_account_balance_with_150_when_make_withdrawal_of_200_should_throw_an_exception_and_no_transaction_created():
    # GIVEN
    bank_account = BankAccount(uuid.uuid4())
    bank_account.make_deposit(150)
    # GIVEN
    # THEN
    with pytest.raises(InsufficientBalanceError) as error:
        bank_account.make_withdrawal(200)
    assert error.value.args[0] == f"Insufficient funds : your current balance is {bank_account.get_balance()}"
    assert len(bank_account.get_trading_operation_history()) == 1


def test_when_create_bank_should_have_empty_list_of_accounts():
    # GIVEN
    bank = Bank()

    # WHEN-THEN
    assert not bank.get_accounts()


def test_given_bank_when_create_account_should_append_list_accounts():
    # GIVEN
    bank = Bank()

    # WHEN
    iban = bank.create_account()

    # THEN
    assert len(bank.get_accounts()) == 1
    assert isinstance(list(bank.get_accounts().values())[0], BankAccount)
    assert isinstance(iban, uuid.UUID)


def test_given_account_in_bank_when_get_account_by_iban_should_return_account():
    # GIVEN
    bank = Bank()
    iban = bank.create_account()

    # WHEN
    account = bank.get_account_by_iban(iban)

    # THEN
    assert account.get_iban() == iban


def test_given_wrong_iban_when_get_account_by_iban_should_raise_KeyError():
    # GIVEN
    bank = Bank()

    # WHEN-THEN
    with pytest.raises(KeyError) as error:
        account = bank.get_account_by_iban(uuid.uuid4())
    assert error.value.args[0] == "iban not found in accounts"


class TestTransaction(TestCase):
    @patch.object(TimeService, 'get_time_now')
    def test_given_deposit_150_should_return_trading_operation_history(self, get_time_now_mock):
        # GIVEN

        get_time_now_mock.return_value = datetime.datetime.strptime("25/06/2021 07:58:56.450",
                                                                    "%d/%m/%Y %H:%M:%S.%f")

        bank_account = BankAccount(uuid.uuid4())
        expected_dates = [datetime.datetime.strptime("12/07/2021 07:58:56.450",
                                                     "%d/%m/%Y %H:%M:%S.%f"),
                          datetime.datetime.strptime("25/06/2021 07:58:56.450",
                                                     "%d/%m/%Y %H:%M:%S.%f")]
        expected_history = pd.DataFrame(
            data={"Date": expected_dates, "Transaction": [460, 150], "Balance": [610, 150]})
        # WHEN
        bank_account.make_deposit(150)

        get_time_now_mock.return_value = datetime.datetime.strptime("12/07/2021 07:58:56.450",
                                                                    "%d/%m/%Y %H:%M:%S.%f")
        bank_account.make_deposit(460)
        trading_history = bank_account.get_trading_operation_history()
        # THEN
        assert trading_history.equals(expected_history)

    @patch.object(TimeService, 'get_time_now')
    def test_given_deposit_and_withdrawal_should_return_trading_operation_history(self, get_time_now_mock):
        # GIVEN

        get_time_now_mock.return_value = datetime.datetime.strptime("25/06/2021 07:58:56.450",
                                                                    "%d/%m/%Y %H:%M:%S.%f")

        bank_account = BankAccount(uuid.uuid4())
        expected_dates = [datetime.datetime.strptime("12/07/2021 07:58:56.450",
                                                     "%d/%m/%Y %H:%M:%S.%f"),
                          datetime.datetime.strptime("25/06/2021 07:58:56.450",
                                                     "%d/%m/%Y %H:%M:%S.%f")]
        expected_history = pd.DataFrame(
            data={"Date": expected_dates, "Transaction": [-460, 5650], "Balance": [5190, 5650]})

        # WHEN
        bank_account.make_deposit(5650)
        get_time_now_mock.return_value = datetime.datetime.strptime("12/07/2021 07:58:56.450",
                                                                    "%d/%m/%Y %H:%M:%S.%f")
        bank_account.make_withdrawal(460)
        trading_history = bank_account.get_trading_operation_history()
        # THEN
        assert trading_history.equals(expected_history)

# DONE open a bank account with amount at 0
# DONE obtain balance in bank account
# DONE make deposit of 10 recorded /with today's date
# DONE cannot make deposit <= 0
# DONE make withdrawal of 5 recorded /with today's date
# DONE cannot make withdrawal <= 0
# DONE handle exception when insufficient balance for withdrawal
# return list of all transactions sorted by date
