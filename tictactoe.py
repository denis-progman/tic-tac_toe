class TicTacToe:
    def __init__(self, area, players):
        self.area = area
        self.players = players
        self.current_player = 0
        for player in self.players:
            player.fill_storage(self.area.get_size())        

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

    def position_request(self, player):
        if len(self.area.get_taken_positions()) == self.area.get_space():
            raise Warning("\n\nAll positions are taken, it over!\nWe have a draw!\n\n")
        print(f'The turn of {player.get_mark()} player..')
        if type(player).__name__ == "AutoPlayer":
            return player.next_position(self.area.get_taken_positions(), self.area.get_space())
        position = input(f'Enter position (0 - {self.area.get_space() - 1}): ')
        if not position.isnumeric():                    
            raise UserWarning("Wrong symbol!")
        position = int(position)
        if position > self.area.get_space() or position < 0:
            raise UserWarning("Wrong number!")
        return position
    
    def play(self):
        self.area.print_board()
        while True:
            try:
                position = self.position_request(self.players[self.current_player])
                self.score_count(position)
                self.area.took_position(position, self.players[self.current_player].get_mark()).print_board()
                if self.players[self.current_player].is_winner(self.area.get_size()):
                    print(f'\n\n\nThe winner is {self.players[self.current_player].mark}! Cool!\n\n\n')
                    break
                self.next_player()
            except UserWarning as warning:
                print(f'{warning}\n')
                self.area.print_board()
