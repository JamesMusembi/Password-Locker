#!/usr/bin/env python3.9

# import email
from credentials import Account


def create_account(fname,lname,username,password,email):
    '''
    Function to create a new account
    '''
    new_account =Account(fname,lname,username,password,email)
    return new_account
def save_accounts(account):
    '''
    Function to save the new account
    '''
    account.save_account()
def delete_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()
def display_accounts():
    
    return Account.display_accounts()

def find_account(username):
  
    return Account.find_by_username(username)

def check_existing_accounts(username):
    
    return Account.account_exist(username)

print()
print('PASSWORD LOCKER APPLICATION')
print("")

def main():
    print("Hello welcome,Enter your name to create an account")
    user_name=input()
    print(f"Hello {user_name}. what would you like to do?")
    print("\n")

    while True:
        print("Use these short codes : ca - create a new account,gp -generate new password ,cpg - get generated password by computor, da - display accounts,dp -display old password, fa -find an account, ex -exit the account list ")