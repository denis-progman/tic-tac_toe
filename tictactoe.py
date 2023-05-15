from area import Area
from player import Player


class TicTacToe:
    def __init__(self, area: Area, players: list[Player]):
        self.area = area
        self.players = players
        self.current_player = 0

    def next_player(self):
        self.current_player = self.current_player + 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def position_request(self, player: Player):
        if self.area.is_full():
            raise Warning("\n\nAll positions are taken, it over!\nWe have a draw!\n\n")
        print(f'The turn of {player.get_mark()} player..')
        return player.next_position(self.area, self.players)
    
    def play(self):
        self.area.print_board()
        while True:
            try:
                position = self.position_request(self.players[self.current_player])
                self.area.take_position(position, self.players[self.current_player]).print_board()
                if self.players[self.current_player].is_winner(self.area.get_size()):
                    print(f'\n\n\nThe winner is {self.players[self.current_player].mark}! Cool!\n\n\n')
                    break
                self.next_player()
            except UserWarning as warning:
                print(f'{warning}\n')
                self.area.print_board()
