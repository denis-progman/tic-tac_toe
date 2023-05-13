import random
import time
import math
from player import Player
from area import Area

class IntelligentAutoPlayer(Player):
    def __init__(self, mark):
        super().__init__(mark)

    def next_position(self, area: Area):
        time.sleep(1)
        positions = [0]*area.get_space()
        for position in positions:

            position = [[-1]*5] 
            positions[position][0] = position + 1 // area.get_size()
            positions[position][1] = position % area.get_size()
            
            if (positions[position][0] == positions[position][1]):
                positions[position][2] = 0
            if (positions[position][0] + positions[position][1] == area.get_size() - 1):
                positions[position][3] = 0
            positions[position][4] = 1
            

            position = random.randint(0, area.get_space() - 1)
            if position not in area.get_taken_positions():
                return position













        win_ways = [0]*(matrix_size * 2 + 2)
        prevent_ways = [0]*(matrix_size * 2 + 2)
        possible_ways = [matrix_size]*(matrix_size * 2 + 2)
        for player in players:
            for score_index, score in enumerate(player.get_scores()):
                max_player_score = max(player.get_scores())
                possible_ways[score_index] -= score
                if score == max_player_score:
                    if player == self:
                        win_ways[score_index] = score
                    else:
                        prevent_ways[score_index] = score
        
        # max_score = max(scores)
        print(win_ways)
        print(prevent_ways)
        print(possible_ways)
        potential_score_indexes = []
        while True:
            for score_index, score in enumerate(scores): 
                if  score == max_score and whole_scores[score_index] != matrix_size:
                    potential_score_indexes.append(score_index)
            if potential_score_indexes:
                break
            max_score -= 1

        score_index = potential_score_indexes[random.randint(0, len(potential_score_indexes) - 1)]
        position_type = score_index // matrix_size # 0 - row / 1 - coll / 2 - diagonal
        position_index = score_index % matrix_size  # number of row / coll / diagonal
        print(f'score_index: {score_index}')
        print(f'position_type: {position_type} position_index: {position_index}')

        if position_type == 0: # row
            the_range = range(position_index * matrix_size, matrix_size)
        elif position_type == 1: # coll
            the_range = range(position_index, space - matrix_size, matrix_size)
        elif position_index == 0: # diagonals
            the_range = range(0, space, matrix_size + 1)
        else: 
            the_range = range(matrix_size, space - matrix_size, matrix_size - 1)

        the_range = list(the_range)

        print(f'Range: {the_range}')
        return the_range[random.randint(0, len(the_range) - 1)] # the final chose                

