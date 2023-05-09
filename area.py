
class Area:
    BLANK_SQUARE = '_'
    HORIZON_SPACE = 8
    VERTICAL_SPACE = 2

    def __init__(self, size):
        self.size = size
        self.board = [self.BLANK_SQUARE] * self.size ** 2

    def get_size(self):
        return self.size
    
    def print_board(self, players_positions = []):
        print()
        for i in range(0, self.size ** 2):
            print(self.board[i], end=' '* self.HORIZON_SPACE)
            if i % self.size == self.size - 1:
                print("\n" * self.VERTICAL_SPACE)