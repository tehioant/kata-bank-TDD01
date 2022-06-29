import pytest as pytest

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


def test_given_bank_account_balance_when_make_deposit_should_return_balance():
    # GIVEN
    bank_account = BankAccount()

    # WHEN
    bank_account.make_deposit(1000)

    # THEN
    assert bank_account.get_balance() == 1000


def test_given_bank_account_balance_when_make_deposit_of_invalid_value_should_throw_exception():
    # GIVEN
    bank_account = BankAccount()
    invalid_deposit_values = [-2, 0]

    # WHEN - THEN
    for deposit_value in invalid_deposit_values:
        with pytest.raises(ValueError) as error:
            bank_account.make_deposit(deposit_value)
        assert error.value.args[0] == "Deposit value should be positive"




# DONE open a bank account with amount at 0
# DONE obtain balance in bank account
# DONE make deposit of 10 recorded /with today's date
# cannot make deposit <= 0
# make withdrawal of 5 recorded /with today's date
# cannot make withdrawal <= 0
# handle exception when insufficient balance for withdrawal
# return list of all transactions sorted by date
