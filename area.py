from memory_handler import MemoryHandler
from player import Player

class Area:
    BLANK_SQUARE = '_'
    HORIZON_SPACE = 8
    VERTICAL_SPACE = 2

    def __init__(self, size: int):
        self.size = size
        self.space = self.size ** 2
        self.positions = [0] * self.space
        self.available_positions_base = MemoryHandler.create_positions_base(self.size, self.space)
    
    def get_size(self):
        return self.size
    
    def get_space(self):
        return self.space
    
    def get_positions(self):
        return self.positions
    
    def get_available_positions_base(self):
        return self.available_positions_base
    
    def get_available_positions(self):
        return [position for position, position_owner in enumerate(self.positions) if not position_owner]
    
    def is_full(self):
        return not 0 in self.positions  
    
    def take_position(self, position: int, player: Player):
        if self.positions[position]:
            raise UserWarning("This position is already taken! Please choose another one.")
        self.positions[position] = player
        position_index = MemoryHandler.create_position_index(self.size, position)
        self.available_positions_base = MemoryHandler.erase_positions_base(self.available_positions_base, position)
        player.add_scores(position_index)
        return self

    def print_board(self):
        print()
        for i in range(0, self.space):
            print_mark = self.BLANK_SQUARE
            if self.positions[i]:
                print_mark = self.positions[i].get_mark()
            print(print_mark, end=' '* self.HORIZON_SPACE)
            if i % self.size == self.size - 1:
                print("\n" * self.VERTICAL_SPACE)
                