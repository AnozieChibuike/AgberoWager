import unittest
from unittest.mock import patch
from models.user import User
from create import create_user


class TestUserModel(unittest.TestCase):
    
    @patch('builtins.input',side_effect=['John','18','Nigeria'])
    def test_create_user(self,mock):
        User.users = []
        create_user()
        self.assertEqual(len(User.users),1)
        
    @patch('builtins.input',side_effect=['Johnny','12','Nigeria'])
    def test_create_user_incorrect(self,mock):
        print(User.users)
        with self.assertRaises(PermissionError):
            create_user()

    def test_create_error(self):
        with self.assertRaises(AttributeError):
            User()
    def test_create_without_error(self):
        user = User(username='Joel',country='Nigeria',age=20,currency='Naira')
        self.assertIn(user,User.users,'Should not be none if exists')
        
    def test_user_list(self):
        User.users = []
        user = User(username='Joel',country='Nigeria',age=20,currency='Naira')
        user2 = User(username='Joelan',country='Nigeria',age=20,currency='Naira')
        self.assertListEqual([user,user2],User.users)
        
        
if __name__ == '__main__':
    unittest.main()