from bank.main import BankAccount


class test_bank:

    def test_create_bank_account_with_ammout_at_Zero(self):
        # GIVEN

        # WHEN
        bank_account = BankAccount()

        # THEN
        assert bank_account.balance == 0

# open a bank account with amount at 0
# obtain balance in bank account
# make deposit of 10 recorded with today's date
# cannot make deposit <= 0
# make withdrawal of 5 recorded with today's date
# cannot make withdrawal <= 0
# handle exception when insufficient balance for withdrawal
# return list of all transactions sorted by date
