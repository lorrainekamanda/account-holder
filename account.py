class Account:
    account_list = []
    """
    this is an empty array used to store the saved accounts
    """
    def __init__(self,user_name,password):
          """
          initialize the object in the class by using self 
          """
          self.user_name = user_name
          self.password = password
    def save_account(self):
          """
          this appends the available in the empty array created
          """
          Account.account_list.append(self)
    def remove_account(self):
          """
          this method removes any saved account
          """
          Account.account_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        for account in cls.account_list:
            if account.user_name == number:
                 return account
        """
        this method ensures you can search for your account using only your username
        """

    @classmethod
    def display_account(cls):
        return cls.account_list
        """
        this method returns all saved accounts
        """
class Credential:

    def __init__(self,first_name,last_name,email,phone_number):
        """
        initializing the credential object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    credential_list = []
    """
    empty array where credentials will be stored
    """

    def save_account(self):
        Credential.credential_list.append(self)
        """
        saving credentials
        """

    def remove_account(self):
        """
        deleting credentials
        """
        Credential.credential_list.remove(self)
     