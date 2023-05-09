BLANK_SQUARE = '_'


class TicTacToe:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [BLANK_SQUARE] * self.board_size ** 2
        self.current_player = 'X'

    def print_board(self):
        print()
        for i in range(0, self.board_size ** 2):
            print(self.board[i], end='  ')
            if i % self.board_size == self.board_size - 1:
                print()
                print()

    def make_move(self, position):
        if self.board[position] == BLANK_SQUARE:
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print('Invalid move!')

    def check_winner(self):
        # Check rows
        for i in range(0, self.board_size ** 2, self.board_size):
            count_same = 1
            for j in range(i + 1, i + self.board_size):
                if self.board[j] == self.board[j-1] != BLANK_SQUARE:
                    count_same += 1
            if count_same == self.board_size:
                return self.board[i]

        # Check columns
        for i in range(self.board_size):
            count_same = 1
            for j in range(i + self.board_size, self.board_size ** 2, self.board_size):
                if self.board[j] == self.board[j - self.board_size] != BLANK_SQUARE:
                    count_same += 1
            if count_same == self.board_size:
                return self.board[i]

        # Check diagonals
        count_same = 0
        for i in range(0, self.board_size ** 2, self.board_size + 1):
            if self.board[i] == self.board[0] != BLANK_SQUARE:
                count_same += 1
        if count_same == self.board_size:
            return self.board[0]

        count_same = 0
        for i in range(self.board_size - 1, self.board_size ** 2 - 1, self.board_size - 1):
            if self.board[i] == self.board[self.board_size - 1] != BLANK_SQUARE:
                count_same += 1
        if count_same == self.board_size:
            return self.board[self.board_size - 1]

        return None

    def check_draw(self):
        return BLANK_SQUARE not in self.board

    def reset(self):
        self.board = [BLANK_SQUARE] * 9
        self.current_player = 'X'


# Main program starts here
board_size = int(input('What board size do you want? '))

game = TicTacToe(board_size=board_size)

# Game loop
while game.check_winner() is None and not game.check_draw():
    game.print_board()
    position = int(input(f'Enter position (0 - {game.board_size ** 2 - 1}): '))
    game.make_move(position)

game.print_board()
