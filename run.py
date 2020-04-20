#!/usr/bin/env python3.6
import math
import random
from account import Account
from account import Credential

def create_account(username,password):
    """
    function creating a new account
    """
    new_account = Account(username,password)
    return new_account
def delete_account(account):
    """
    function to remove account

    """
    account.remove_account()

def create_credential(first_name,last_name,email,phone_number,account_name,account_username,account_password):
    """
    function allows one to create credentials
    """
    new_credential = Credential(first_name,last_name,email,phone_number,account_name,account_username,account_password)
    return new_credential

def remove_credential(credential):
    """
    function to delete credentials
    """
    credential.remove_account()
def save_account(account):
    """
    this function saves a new account
    """
    account.save_account()

def save_credential(credential):
    """
    saving credentials
    """
    credential.save_account()

def find_account(password):
    """
    check if account exists inorder to log in
    """
    return Account.account_exist(password)

def account_exist(password):
    """
    check if contact exists
    """
    return Account.account_exist(password)

def display_account():
    return Account.display_account()

def display_credential():
    return Credential.display_credential()







def main():

    print("Hi,we are Account holder,responsible for saving all your account usernames and  ....what is your name?")
    name = input()

    print(f"Hello {name},welcome to Account holder...")

    print("\n")

    while True:

                print("do you want to create an account?")

                print("type ca if you want a new account,lg to login ,va to view accounts,ra to delete,cc to create credentials ")
                key = input()
                if key == 'ca':
                   print("New Account")
                   print("-"*10)
                   print("Create account username ")
                   
                   username =input()
                   print("type cp to create your own password or gp to have password generated for you,cc to create new credentials")

                   password = input()

                   if password == "cp":
                       print("create password")
                       password = input()

                   elif password == "gp":
                      password = str(random.randint(1,1000))

                   else:
                      print("please enter a valid option")


                   save_account(create_account(username,password))
                   print ('\n')
                   print(f"Account username:.{username}.... Password:.{password}")
                
                elif key == 'va':
                    if display_account():
                        for account in display_account():
                            print("here are/is the account created...")
                            print("\n")

                            print(f"Username:{account.user_name} , Password:{account.password}")

              

                    else:
                        print("account doesnt exist")

                elif key == "lg":
                   
                    print ("key in password")
                    password = input()
                    if account_exist(password):
                        print(f"Welcome:{username}, Password{password} you have sucessfully loged into your account")
                    else:
                        print("ooops no such account")
                
                elif key == "ra":
                    print("username to delete")

                    username = input()

                    print("password")

                    password = input()
                    if account_exist(username):
                         
                        get_account = account_exist(username)
                        delete_account(get_account)
                        print(f"deleted {get_account.username} and {get_account.password} successfully")
                       
                       
                    else:
                        ("no such account")
                        
                        
                    

                      
                
                elif key == 'cc': 
                   print("Credentials")
                   print('key in cc to create credential,vc to view credential,rc to remove credentials')
                
                
                   print('new credentials')

                   print("\n")

                   print('First Name..')

                   first_name = input()

                   print("Last Name...") 

                   last_name = input()

                   print('Email..')

                   email = input()

                   print("Phone Number...") 

                   phone_number = input()

                   print('Account Name..')

                   account_name = input()

                   print("Account Username...") 

                   account_username = input()

                   print("Account Password...") 

                   account_password = input()

                   save_credential(create_credential(first_name,last_name,email,phone_number,account_name,account_username,account_password))

                   print('account and credential saved,any other option')

                   option = input()

                   if option == "rc":
                         
                       remove_credential(create_credential(first_name,last_name,email,phone_number,account_name,account_username,account_password))

                elif key == 'vc':
                    if display_credential():
                        for credential in  display_credential():
                            print("The Credentials")
                            print(f" Identity:{credential.first_name,credential.last_name}")
                            print(f" Contacts:{credential.email,credential.phone_number}")
                            print(f" Account:{credential.account_name},{credential.account_username},{credential.account_password}")
            


                else:
                    print('not an option')



                    print ('\n')
                   



                
                




if __name__ == '__main__':

    main()


