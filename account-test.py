from account import Account
import unittest
"""
import unnittest and Account class
"""

class testAccount(unittest.TestCase):

    def setUp(self):
        """
        check if the initialzation is correct
        """

    
        self.new_account = Account('lorraine','leilanjeri123')

    def test__init(self):
        """
        check if the system is initialiazing correctly
        """  

        self.assertEqual(self.new_account.user_name,'lorraine')
        self.assertEqual(self.new_account.password,'leilanjeri123')

        Account.account_list =[]
    
    def test__save_account(self):
        """
        this test checks to see if the account is saved 
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        Account.account_list = []

    def test__saveMultiple_accounts(self):
        """
        this tests checks whether the test can save multiple accounts
        and/assert equal to make sure we have two accounts
        """
        self.new_account.save_account()
        test_another_account = Account('grace','newzealand2020')
        test_another_account.save_account()
        self.assertEqual(len(Account.account_list),2)
    


if __name__ == '__main__':
    unittest.main()