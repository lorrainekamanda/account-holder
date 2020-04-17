class Account:
    
    def __init__(self,user_name,password):
          self.user_name = user_name
          self.password = password
    def save_account(self):
          Account.account_list = []
          Account.account_list.append(self)
     