import random
from area import Area
from auto_player import AutoPlayer
from player import Player
from memory_handler import MemoryHandler

class IntelligentAutoPlayer(AutoPlayer):
    
    __level: int # 1 - 5

    def __init__(self, mark, area_size, level: int = 1):
        super().__init__(mark, area_size)
        self.__level = level

    def get_level(self):
        return self.__level
    
    @staticmethod
    def _get_best_ways(score_index):
        return [score if score == max(score_index) else 0 for score in score_index]
    
    def next_position(self, area: Area, players: list[Player]):
        self._pause()
        area_size = area.get_size()
        available_positions = area.get_available_positions()
        if self.__level <= 0:
            print(f"just random ;)")
            return self._get_random_choice(available_positions)
        
        other_players = players[:] # to calculate my self separately
        other_players.pop(self.get_id())

        others_bests = []
        total_scores = MemoryHandler.create_storage(area_size)
        for other in other_players: # now is's others players
            scores = other.get_scores()
            self._sum_scores(total_scores, scores)
            others_bests.append(self._get_best_ways(scores))
        
        my_bests = self._get_best_ways(self.scores)
        self._sum_scores(total_scores, self.scores) 

        best_choose = None
        rasing_chosen_ways = []
        obstructing_chosen_ways = []
        rasing_obstructing_chosen_ways = []

        break_flag = False
        for way_num in range(0, len(self.scores)):
            if total_scores[way_num] == area_size:
                continue  
            if self.__level <= 1 and my_bests[way_num] + 1 == area_size:
                best_choose = way_num
                break
            if self.__level <= 2 and (not total_scores[way_num] or (my_bests[way_num] and total_scores[way_num] == my_bests[way_num] and not way_num in rasing_chosen_ways)):
                rasing_chosen_ways.append(way_num)
            for other_bests in others_bests:
                if self.__level <= 3 and other_bests[way_num] + 1 == area_size:
                    best_choose = way_num
                    break_flag = True
                    break  
                for other_bests in others_bests:
                    if self.__level <= 4 and other_bests[way_num] and total_scores[way_num] == other_bests[way_num] and not way_num in obstructing_chosen_ways:
                        obstructing_chosen_ways.append(way_num)          
            if break_flag:
                break        


        the_choose = None
        available_positions_base = area.get_available_positions_base()

        if best_choose is not None:
            the_choose = best_choose
            print(f"privet or win by {the_choose} way")

        if self.__level <= 5:
            for available_position_ways in available_positions_base:
                for available_position_way in available_position_ways:
                    if available_position_way in rasing_chosen_ways and available_position_way in obstructing_chosen_ways:
                        rasing_obstructing_chosen_ways.append(available_position_way)
        
        
        if not the_choose and rasing_obstructing_chosen_ways:
            the_choose = self._get_random_choice(rasing_obstructing_chosen_ways)
            print(f"raising & privet by {the_choose} way")
        elif not the_choose and rasing_chosen_ways:
            the_choose = self._get_random_choice(rasing_chosen_ways)
            print(f"raising by {the_choose} way")
        elif not the_choose and obstructing_chosen_ways:
            the_choose = self._get_random_choice(obstructing_chosen_ways)
            print(f"obstructing by {the_choose} way")
            
        if the_choose:
            return self._get_random_choice(available_positions_base[the_choose])
        
        print(f"just random :(")
        return self._get_random_choice(available_positions)
        