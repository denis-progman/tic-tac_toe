import random
import time
from area import Area
from player import Player

class AutoPlayer(Player):
    def __init__(self, mark, area_size):
        super().__init__(mark, area_size)

    def next_position(self, positions: list):
        time.sleep(1)
        while True:
            position = random.randint(0, len(positions) - 1)
            if not positions[position]:
                return position
        
