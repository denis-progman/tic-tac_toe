import random
import time
from player import Player

class AutoPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)

    def next_position(self, taken_positions, space):
        time.sleep(1)
        while True:
            position = random.randint(0, space - 1)
            if position not in taken_positions:
                return position
        
