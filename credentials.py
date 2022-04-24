import unittest

class Account:

    account_list=[]
    
    def __init__(self,first_name,last_name,username,      
                 email,password):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.password=password

    def save_account(self):
        self.account_list.append(self)


    def delete_account(self):
        self.account_list.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_list

    @classmethod
    def find_by_username(cls,username):
        for account in cls.account_list:
            if account.username == username:
                return account

    @classmethod
    def account_exist(cls,username):

        for account in cls.account_list:
            if account.username == username:
                return True
        return False