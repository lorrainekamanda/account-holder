class Account:
    account_list = []
    def __init__(self,user_name,password):
          self.user_name = user_name
          self.password = password
    def save_account(self):
          Account.account_list.append(self)
    def remove_account(self):
          Account.account_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        for account in cls.account_list:
            if account.user_name == number:
                return account

     