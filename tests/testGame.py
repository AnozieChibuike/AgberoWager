import unittest
from unittest.mock import patch
from models.user import User
from main import playGame
from create import create_user
from games.dice import Dice


class TestGame(unittest.TestCase):
    
    @patch('builtins.input',side_effect=['Johnnyo','18','Nigeria','Computer','20','Mali'])
    def test_multiple_create_user(self,mock):
        User.users = []
        create_user()
        create_user()
        self.assertEqual(len(User.users),2)
        
    
    @patch('builtins.input',side_effect=['200','yes'])
    def test_play_game(self,mock):    
        User.users[0].balance = 2000
        User.users[1].balance = 2000
        game = playGame(User.users[0],User.users[1])
        self.assertIsInstance(game,Dice)
        print(User.users[0].balance)
        print(User.users[1].balance)
    
    @patch('builtins.input',side_effect=['200','yes'])
    def test_play_game_low_balance(self,mock):    
        User.users[0].balance = 0
        User.users[1].balance = 2000
        with self.assertRaises(InterruptedError):
            playGame(User.users[0],User.users[1])
            
    @patch('builtins.input',side_effect=['20','yes','100','yes'])
    def test_play_game_low_stake(self,mock):    
        User.users[0].balance = 2000
        User.users[1].balance = 2000
        game = playGame(User.users[0],User.users[1])
        self.assertIsInstance(game,Dice)
        print(User.users[0].balance)
        print(User.users[1].balance)
    
if __name__ == '__main__':
    unittest.main()