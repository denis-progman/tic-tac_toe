from memory_handler import MemoryHandler

class Player:
    id_source = None
    def __init__(self, mark: str, area_size: int):
        self.id = self.create_id()
        self.mark = mark
        self.scores = MemoryHandler.create_storage(area_size) 

    def get_id(self):
        return self.id
    
    def get_mark(self):
        return self.mark

    def get_scores(self):
        return self.scores
    
    @classmethod
    def create_id(self): 
        if self.id_source is None: 
            self.id_source = 0
        else:
            self.id_source += 1
        return self.id_source

    def add_scores(self, position_index: list):
        for score_num, _ in enumerate(self.scores):
            self.scores[score_num] += position_index[score_num]
        return self.scores
    
    def is_winner(self, area_size: int):
        return area_size in self.scores
    
    def next_position(self, area, all_players: list):
        position = input(f'Enter position (1 - {area.get_space()}): ')
        if not position.isnumeric():                    
            raise UserWarning("Wrong symbol!")
        position = int(position)
        if position > area.get_space() or position < 1:
            raise UserWarning("Wrong number!")
        return position - 1
    