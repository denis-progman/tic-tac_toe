class Area:
    BLANK_SQUARE = '_'
    HORIZON_SPACE = 8
    VERTICAL_SPACE = 2

    def __init__(self, size):
        self.size = size
        self.space = self.size ** 2
        self.taken_positions = {}

    def get_size(self):
        return self.size
    
    def get_space(self):
        return self.space
    
    def get_taken_positions(self):
        return self.taken_positions
    
    def took_position(self, position, mark):
        if position in self.taken_positions:
            raise UserWarning("This position is already taken! Please choose another one.")
        self.taken_positions[position] = mark
        return self

    def print_board(self):
        print()
        for i in range(0, self.space):
            print_mark = self.BLANK_SQUARE
            if i in self.taken_positions:
                print_mark = self.taken_positions[i]
            print(print_mark, end=' '* self.HORIZON_SPACE)
            if i % self.size == self.size - 1:
                print("\n" * self.VERTICAL_SPACE)