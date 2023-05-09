class Player:
    def __init__(self, mark):
        self.type = mark
        self.positions = []

    def make_move(self, position):
        if position in self.positions:
            raise Exception('Invalid move!')
        self.positions.append(position)
        return self.positions