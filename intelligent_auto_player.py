import random
import time
import math
from player import Player
from area import Area

class IntelligentAutoPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)

    def next_position(self, positions: list):
        time.sleep(1)
        for position in positions:
            pass
