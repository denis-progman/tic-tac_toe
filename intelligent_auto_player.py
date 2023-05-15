import random
from area import Area
from auto_player import AutoPlayer
from player import Player
from memory_handler import MemoryHandler

class IntelligentAutoPlayer(AutoPlayer):
    
    def __init__(self, mark, area_size, level: int):
        super().__init__(mark, area_size)

    def next_position(self, area: Area, players: list[Player]):
        self._pause()
        area_size = area.get_size() 
        other_players = players[:]
        other_players.pop(self.get_id()) # to make it others players

        others_bests = []
        total_scores = MemoryHandler.create_storage(area_size)
        for other in other_players: # now is's others players
            scores = other.get_scores()
            total_scores = list(map(sum, zip(scores, total_scores)))
            others_bests.append([score if score == max(scores) else 0 for score in scores])
        
        my_bests = [score if score == max(self.scores) else 0 for score in self.scores]

        for total_score_num, _ in enumerate(total_scores):
            total_scores[total_score_num] += self.scores[total_score_num]

        best_choose = None
        rasing_chosen_ways = []
        obstructing_chosen_ways = []
        break_flag = False
        for way_num in range(0, len(self.scores)):
            if total_scores[way_num] == area_size:
                continue  
            if  my_bests[way_num] + 1 == area_size:
                best_choose = way_num
                break
            for other_bests in others_bests:
                if other_bests[way_num] + 1 == area_size:
                    best_choose = way_num
                    break_flag = True
                    break
                if other_bests[way_num] and total_scores[way_num] == other_bests[way_num] and not way_num in obstructing_chosen_ways:
                    obstructing_chosen_ways.append(way_num)
            if my_bests[way_num] and total_scores[way_num] == my_bests[way_num] and not way_num in rasing_chosen_ways:
                rasing_chosen_ways.append(way_num)

            if break_flag:
                break

        the_choose = None
        if best_choose is not None:
            the_choose = best_choose
            print(f"privet or win by {the_choose} way")
        elif rasing_chosen_ways:
            the_choose = rasing_chosen_ways[random.randint(0, len(rasing_chosen_ways) - 1)]
            print(f"raising by {the_choose} way")
        elif obstructing_chosen_ways:
            the_choose = obstructing_chosen_ways[random.randint(0, len(obstructing_chosen_ways) - 1)]
            print(f"obstructing by {the_choose} way")
        else:
            print(f"just random :(")

        
        if the_choose is not None:
            available_positions_base = area.get_available_positions_base()
            return available_positions_base[the_choose][random.randint(0, len(available_positions_base[the_choose]) - 1)]
        return self._get_random_position(area.get_available_positions())
        

        

        
   
                        











                
                