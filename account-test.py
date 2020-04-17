from account import Account
import unittest
"""
import unnittest and Account class
"""

class testAccount(unittest.TestCase):

    def setUp(self):
        """
        setup is what will be runned before each test
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
        """
        tearDown is what will be runned after each test
        """

    def test__saveMultiple_accounts(self):
        """
        this tests checks whether the test can save multiple accounts
        and/assert equal to make sure we have two accounts
        """
        self.new_account.save_account()
        test_another_account = Account('grace','newzealand2020')
        test_another_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test__remove_account(self):
        """
        this test checks whether the the app deletes a saved account
        the length of the remaining array should be 1
        """
        self.new_account.save_account()
        test_another_account = Account('grace','newzealand2020')
        test_another_account.save_account()
        self.new_account.remove_account()
        self.assertEqual(len(Account.account_list),1)

    def test__search_account_by_username(self):
         """
         search a saved account by number
         """
         self.new_account.save_account()
         test_another_account = Account('grace','newzealand2020')
         test_another_account.save_account()


        
         get_account = Account.find_by_number('grace')
         self.assertEqual(get_account.password,test_another_account.password)


if __name__ == '__main__':
    unittest.main()