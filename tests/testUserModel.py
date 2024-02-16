import unittest
from unittest.mock import patch
from models.user import User
from create import create_user


class TestUserModel(unittest.TestCase):
    
    @patch('builtins.input',side_effect=['John','18','Nigeria'])
    def test_create_user(self,mock):
        self.assertIsInstance(create_user(),dict)
        
    @patch('builtins.input',side_effect=['Johnny','12','Nigeria'])
    def test_create_user_incorrect(self,mock):
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
        
    def test_create_user_from_dict(self):
        User.users = []
        user=User(from_dict={'username':'Joel','age':19,'country':'Naija'})
        self.assertIn(user,User.users)
        
    @patch('builtins.input',side_effect=['Johnny','18','Nigeria'])
    def test_create_user_from_create_user_return_value(self,mock):
        User.users = []
        user=User(from_dict=create_user())
        self.assertIn(user,User.users)
        
    def test_create_user_from_dict_error(self):
        User.users = []
        with self.assertRaises(KeyError):
            User(from_dict={'age':19,'country':'Naija'})
            
    def test_create_user_from_dict_not_dict_param(self):
        with self.assertRaises(TypeError):
            User(from_dict='Jol')
