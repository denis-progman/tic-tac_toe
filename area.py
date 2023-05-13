from player import Player


class Area:
    BLANK_SQUARE = '_'
    HORIZON_SPACE = 8
    VERTICAL_SPACE = 2

    def __init__(self, size):
        self.size = size
        self.space = self.size ** 2
        self.positions = [0] * self.space
    
    def get_size(self):
        return self.size
    
    def get_space(self):
        return self.space
    
    def get_positions(self):
        return self.positions
    
    def is_full(self):
        return not 0 in self.positions

    def make_position_index(self, position, player: Player):
        index = [0] * (self.size * 2 + 3)
        row = position // self.size
        coll = position % self.size
        index[row] = 1
        index[row + coll] = 1
        if row == coll:
            index[row + coll + 1] = 1
        if row + coll == self.size - 1:
            index[row + coll + 2] = 1
        index[len(index) - 1] = player
        return index   
    
    def take_position(self, position, player: Player):
        if self.positions[position]:
            raise UserWarning("This position is already taken! Please choose another one.")
        self.positions[position] = self.make_position_index(position, player)
        player.add_scores(self.positions[position])
        print(player.get_scores())
        return self

    def print_board(self):
        print()
        for i in range(0, self.space):
            print_mark = self.BLANK_SQUARE
            if self.positions[i]:
                print_mark = self.positions[i][len(self.positions[i]) - 1].get_mark()
            print(print_mark, end=' '* self.HORIZON_SPACE)
            if i % self.size == self.size - 1:
                print("\n" * self.VERTICAL_SPACE)