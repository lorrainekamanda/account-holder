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

if __name__ == '__main__':
    unittest.main()