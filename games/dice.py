"""
    Roll the Dice game, User will role against another user or computer, highest will win
"""

import random
import os
from dotenv import load_dotenv
import uuid
import math

load_dotenv()

class Dice:
    games = []
    def __init__(self,user1,user2,stake):
        self.id = str(uuid.uuid4())
        self.played = False
        self.user1 = user1
        self.user2 = user2
        self.stake = stake
        Dice.games.append(self)
    def set_roll(self,user1_roll,user2_roll):
        self.roll1 = user1_roll
        self.roll2 = user2_roll
        self.played = True
    def get_winner(self):
        if self.roll1 > self.roll2:
            winner = self.user1
        elif self.roll2 > self.roll1:
            winner = self.user2
        elif self.roll1 == self.roll2:
            winner = None
        return winner
        
def roll():
    return math.ceil(random.random() * 6)
