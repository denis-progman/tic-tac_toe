class Area:
    BLANK_SQUARE = '_'

    def __init__(self, size):
        self.size = size
        self.board = [BLANK_SQUARE] * self.board_size ** 2

    def print_board(self, players_positions = []):
        print()
        for i in range(0, self.size ** 2):
            print(self.board[i], end='       ')
            if i % self.size == self.size - 1:
                print()
                print()