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

if __name__ == '__main__':
    unittest.main()