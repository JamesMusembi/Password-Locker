import unittest
from credentials import Account

class AccountsTest(unittest.TestCase):

    def setUp(self):
        self.new_account=Account("James","Sembi","jamo","jamo267","jamo@gmail.com")


    def test_init(self):
        self.assertEqual(self.new_account.first_name,"James")
        self.assertEqual(self.new_account.last_name,"Sembi")
        self.assertEqual(self.new_account.username,"jamo")
       
        # self.assertEqual(self.new_account.email,"jamo@gmail.com")
        self.assertEqual(self.new_account.password,"jamo267")
    def test_save_account(self):
        self.new_account.save_account() # saving the new contact
        self.assertEqual(len(Account.account_list),1)
        # print(Detail.account_list)

    def tearDown(self):
        Account.account_list=[]
    
    def test_save_multiple_account(self):
        self.new_account.save_account()
        test_account=Account("Test","user","user_","0712345678","test@user.com")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)


    def test_delete_account(self):
        self.new_account.save_account()
        test_account=Account("Test","user","user_","0712345678","test@user.com")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_display_account(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)


if __name__=="__main__":
    unittest.main()