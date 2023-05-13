class Player:
    id_source = 0
    def __init__(self, mark, area_size):
        self.id = self.create_id()
        self.mark = mark
        self.scores = self.create_storage(area_size) 

    def get_id(self):
        return self.id
    
    def get_mark(self):
        return self.mark

    def get_scores(self):
        return self.scores
    
    @classmethod
    def create_id(self): 
        self.id_source += 1
        return self.id_source
    
    def create_storage(self, area_size):
        return [0]*(area_size * 2 + 2)   

    def add_scores(self, position_index: list):
        self.scores = map(sum, zip(self.scores, position_index[:-1]))
        return self.scores
    
    def is_winner(self, area_size):
        if area_size in self.scores:
            return True
        return False
    def next_position(self, positions: list):
        space = len(positions)
        position = input(f'Enter position (1 - {space}): ')
        if not position.isnumeric():                    
            raise UserWarning("Wrong symbol!")
        position = int(position)
        if position > space or position < 1:
            raise UserWarning("Wrong number!")
        return position - 1
    