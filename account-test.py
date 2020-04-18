from account import Account
from account import Credential
import unittest
"""
import unnittest and Account class
Account is the user class while credentials is the Credential class
"""

class testAccount(unittest.TestCase):
    # this is the user test

    def setUp(self):
        """
        setup is what will be runned before each test
        """

    
        self.new_account = Account('lorraine1997','leilanjeri123')
        self.new_credential = Credential("Lorraine",'Kamanda','lorrainekamanda@gmail.com','0726889409')

    def test__init(self):
        """
        check if the system is initialiazing the Account and credential Objects correctly
        """  

        self.assertEqual(self.new_account.user_name,'lorraine1997')
        self.assertEqual(self.new_account.password,'leilanjeri123')

        self.assertEqual(self.new_credential.first_name,'Lorraine')
        self.assertEqual(self.new_credential.last_name,'Kamanda')
        self.assertEqual(self.new_credential.email,'lorrainekamanda@gmail.com')
        self.assertEqual(self.new_credential.phone_number,'0726889409')

        Account.account_list =[]
        Credential.credential_list = []
    
    def test__save_account(self):
        """
        this test checks to see if the user account is saved 
        the second part tests whether the credentials are saved
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)

        self.new_credential.save_account()
        self.assertEqual(len(Credential.credential_list),1)


    def tearDown(self):
        Account.account_list = []
        Credential.credential_list =[]
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

        self.new_credential.save_account()
        test_another_credential = Credential('Grace','Claire','gwanjiku33@gmail.com','0721849552')
        test_another_credential.save_account()



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
    
    def test_display_all_accounts(self):
          """
          test will show all available accounts

          """
          self.assertEqual(Account.display_account(),Account.account_list)

    # the credentials test


    


if __name__ == '__main__':
    unittest.main()