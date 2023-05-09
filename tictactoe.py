BLANK_SQUARE = '_'
X_PLAYER = "X"
O_PLAYER = "0"

class TicTacToe:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [BLANK_SQUARE] * self.board_size ** 2
        self.current_player = X_PLAYER


    def print_board(self):
        print()
        for i in range(0, self.board_size ** 2):
            print(self.board[i], end='       ')
            if i % self.board_size == self.board_size - 1:
                print("\n")

    def make_move(self, position):
        if self.board[position] != BLANK_SQUARE:
            raise Exception('Invalid move!')

        self.board[position] = self.current_player
        if self.current_player == X_PLAYER:
            self.current_player = O_PLAYER
        else:
            self.current_player = X_PLAYER

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

    def play(self):
        # Game loop
        while self.check_winner() is None and not self.check_draw():
            try:
                self.print_board()
                position = int(input(f'Enter position (0 - {self.board_size ** 2 - 1}): '))
                self.make_move(position)
            except Exception as inst:
                print(inst)

        self.print_board()

    # def reset(self): // unused
    #     self.board = [BLANK_SQUARE] * 9
    #     self.current_player = X_PLAYER


# Main program starts here

board_size = int(input('What board size do you want? ')  or 3)

game = TicTacToe(board_size=board_size)
game.play()
