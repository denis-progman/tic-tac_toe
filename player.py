class Player:
    def __init__(self, mark, ):
        self.type = mark
        self.positions = []
        self.score_points = []

    def make_move(self, position):
        if position in self.positions:
            raise Exception('You are already here!')
        self.positions.append(position)
        return self.positions
