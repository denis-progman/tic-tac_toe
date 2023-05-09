from area import Area
from player import Player

class TicTacToe:
    def __init__(self, area, players):
        self.area = area
        self.players = players
        self.current_player = 0

    
    def play(self):
        while True:
            self.area.print_board()
            position = int(input(f'Enter position (0 - {self.area.get_size() ** 2 - 1}): '))
            self.players[self.current_player].make_move(position)



    # def check_draw(self):
    #     return BLANK_SQUARE not in self.board

    # def reset(self):
    #     self.board = [BLANK_SQUARE] * 9
    #     self.current_player = 'X'


# Main program starts here
board_size = int(input('What board size do you want? ')) | 3
area = Area(board_size)
player_x = Player("X")
player_0 = Player("0")

game = TicTacToe(area, [player_x, player_0])
game.play()
# Game loop

