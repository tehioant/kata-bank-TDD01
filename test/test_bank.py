from bank.main import BankAccount


def test_create_bank_account_with_ammout_at_Zero():
    # GIVEN

    # WHEN
    bank_account = BankAccount()

    # THEN
    assert bank_account.balance == 0


def test_given_bank_account_with_balance_zero_return_correct_balance():
    # GIVEN
    bank_account = BankAccount()

    # WHEN-THEN
    assert bank_account.get_balance() == 0


def test_given_bank_account_balance_when_make_deposit_should_return_balance():
    # GIVEN
    bank_account = BankAccount()

    # WHEN
    bank_account.make_deposit(1000)

    # THEN
    assert bank_account.get_balance() == 1000


def test_given_bank_account_balance_when_make_deposit_of_negative_value_should_throw_exception():
    # GIVEN
    bank_account = BankAccount()

    # WHEN
    bank_account.make_deposit(-2)

    # THEN

# DONE open a bank account with amount at 0
# DONE obtain balance in bank account
# DONE make deposit of 10 recorded /with today's date
# cannot make deposit <= 0
# make withdrawal of 5 recorded /with today's date
# cannot make withdrawal <= 0
# handle exception when insufficient balance for withdrawal
# return list of all transactions sorted by date
