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
            if account.password == number:
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
    @classmethod
    def account_exist(cls,number):
        for account in cls.account_list:
            if account.password == number:
                return True
        return False

class Credential:

    def __init__(self,first_name,last_name,email,phone_number,account_name,account_username,account_password):
        """
        initializing the credential object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password

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

    @classmethod
    def display_credential(cls):
        return cls.credential_list
        """
        this method ensures that all the credentials of the user can be displayed
        """

    @classmethod
    def find_by_number(cls,number):
        for credential in cls.credential_list:
            if credential.first_name == number:
                return credential
        """
        this method ensures that you can search for credentials using your first name
        """

    # @classmethod
    # def account_exist(cls,number):
    #     for 


    