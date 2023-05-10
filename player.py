class Player:
    def __init__(self, mark, ):
        self.mark = mark
        self.scores = []

    def get_mark(self):
        return self.mark

    def add_score(self, point_address):
        self.scores[point_address] += 1
        return self.scores
    
    def is_winner(self, max_point):
        if max_point in self.scores:
            return True
        return False
