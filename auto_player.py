import random
import time
from area import Area
from player import Player

class AutoPlayer(Player):
    _seconds: int

    def __init__(self, mark, area_size):
        super().__init__(mark, area_size)
        self.set_pause()

    def _get_random_position(self, available_positions):
        return available_positions[random.randint(0, len(available_positions) - 1)]
    
    def set_pause(self, seconds: int = 1):
        self._seconds = seconds

    def _pause(self):
        time.sleep(self._seconds)

    def next_position(self, area: Area, players: list[Player]):
        self._pause()
        return self._get_random_position(area.get_available_positions())
        
