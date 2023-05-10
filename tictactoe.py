from area import Area
from player import Player

class TicTacToe:
    def __init__(self, area, players):
        self.area = area
        self.players = players
        self.current_player = 0

        for player in self.players:
            player.scores = [0]*(self.area.get_size() * 2 + 2)        

    def next_player(self):
        self.current_player = self.current_player + 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def score_count(self, position):
        row = position // self.area.get_size()
        column = position % (self.area.get_size())

        self.players[self.current_player].add_score(row)
        self.players[self.current_player].add_score(self.area.get_size() + column)
        if column == row:
            self.players[self.current_player].add_score(self.area.get_size() * 2)
        if column + row == self.area.get_size() - 1:
            self.players[self.current_player].add_score(self.area.get_size() * 2 + 1)

    def play(self):
        self.area.print_board()
        while True:
            try:
                position = input(f'Enter position (0 - {self.area.get_space() - 1}): ')
                if not position.isnumeric():                    
                    raise UserWarning("Wrong symbol!")
                position = int(position)
                if position > self.area.get_space() or position < 0:
                    raise UserWarning("Wrong number!")
                
                self.score_count(position)
                self.area.took_position(position, self.players[self.current_player].get_mark()).print_board()
                if self.players[self.current_player].is_winner(self.area.get_size()):
                    print(f'\n\n\nThe winner is {self.players[self.current_player].mark}! Cool!\n\n\n')
                    break
                self.next_player()
            except UserWarning as w:
                print(f'{w}\n')
                self.area.print_board()


# Main program starts here
board_size = int(input('What board size do you want? ') or 3)
area = Area(board_size)
player_x = Player("X")
player_0 = Player("0")
# player_y = Player("Y")

game = TicTacToe(area, [
    player_x, 
    player_0, 
    # player_y
])
game.play()

