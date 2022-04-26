#!/usr/bin/python3.9


# import email
import random
from credentials import Account

chars="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ123456789!@#$&"

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
        print("Use these short codes : ca - create a new account, da - display accounts,dp -display old password, fa -find an account, ex -exit the account list ")
        
        short_code=input().lower()
        if short_code== 'ca':
            print('New Account')
            print('-'*15)

            print('First Name....')
            f_name=input()

            print("Last Name....")
            l_name=input()

            print("Username ....")
            username_=input()

            print("Email ....")
            email_=input()
            password_len=int(10)
            
            password=""
            for x in range(0,password_len):
                password_char=random.choice(chars)
                pass_word=password + password_char
                # print("Here is your password:",pass_word)
                print("choose password option")
        
                print("1.Enter your own password")
                print("2.Let the sytem choose for you")
                p_=input("Enter option;     ")
                if p_=="1":
                     password=input(f"Enter password:   ")
                elif p_=="2":
                     password=pass_word
                if p_=="1" or p_== "2":
                    print('you password has been generated successfully')
                    save_accounts(create_account(f_name,l_name,username_,email_,password)) # create and save new account.
                    print ('\n')
                    print(f"New account {f_name} {l_name} created")
                    print ('\n')
                    break
                    
            

        elif short_code=="da":
            if display_accounts():
                print("Here is the list of all your accounts..")
                print("\n")

                for account in display_accounts():
                     print(f"{account.first_name}    {account.last_name}    {account.email}     {account.username}       {account.password}")
                     print('\n')

            else:
                print('\n')
                print("You dont seem to have any accounts yet")
                print('\n')

        elif short_code=="fa":
            print("Enter the username you want to search")
            search_username=input()

            if check_existing_accounts(search_username):
                search_account = find_account(search_username)
                print(f"{search_account.first_name} {search_account.last_name}")
                print('-' * 20)

                print(f"Username.......{search_account.username}")
                print(f"Email address.......{search_account.email}")

            else:
                print("That contact does not exist")

        elif short_code=="ex":
            print("Thank you,byee.....")
            break
        
        else:
            print("I really didn't get that. Please use the short codes")


if __name__=="__main__":
    main()