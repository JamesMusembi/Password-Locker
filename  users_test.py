import unittest


class AccountsTest(unittest.TestCase):
    def setup(self):
        self.new_account=Account("James", "Sembi", "Jamo" "jamo267", "james@gmail.com")

    def test_init(self):
        self.assertEqual(self.new_account.first_name,"James")
        self.assertEqual(self.new_account.last_name,"Sembi")
        self.assertEqual(self.new_account.username,"jamo")
        self.assertEqual(self.new_account.password,"jamo267")
        self.assertEqual(self.new_account.email,"james@gmail.com")