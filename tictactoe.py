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
    
    def get_leaders_by_score(self):
        top_score = 0
        the_bests = []
        for player in self.players:
            score = max(player.get_scores())
            if score > top_score:
                top_score = score
                the_bests = []
            if top_score == score:
                the_bests.append(player.get_mark())
        the_bests.append(top_score)
        return the_bests

    def position_request(self, player: Player):
        if self.area.is_full():
            leaders = self.get_leaders_by_score()
            raise Warning(f"\n\nAll positions are taken, it over!\nThe best result {leaders.pop()}\nhas been taken by: {leaders}\n\n")
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
