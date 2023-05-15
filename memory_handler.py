class MemoryHandler:
    OUTCASTES_KEY = "outcasts"
    WIN_WAYS_KEY = "win_ways"
    BEST_WAYS_KEY = "best_ways"
    TOTAL_SCORES_KEY = "total_scores"

    def create_storage(area_size: int, additional_cells: int = 0):
        return [0] * (area_size * 2 + 2 + additional_cells)
    
    @classmethod
    def create_positions_base(self, area_size, area_space):
        ways = self.create_storage(area_size)
        for position in range(0, area_space):
            for way_id, way in enumerate(self.create_position_index(area_size, position)):
                if way:
                    if not ways[way_id]:
                        ways[way_id] = []
                    ways[way_id].append(position)
        return ways
    
    @classmethod
    def erase_positions_base(self, positions_base, position):
        return [way_positions.remove(position) or way_positions if position in way_positions else way_positions for way_positions in positions_base]
    
    @classmethod
    def create_position_index(self, area_size: int, position: int, additional_cells_data = []):
        index = self.create_storage(area_size, len(additional_cells_data))
        row = position // area_size
        coll = position % area_size
        row_coll_place = area_size * 2
        index[row] = 1
        index[area_size + coll] = 1
        if row == coll:
            index[row_coll_place] = 1
        if row + coll == area_size - 1:
            index[row_coll_place + 1] = 1
        index += additional_cells_data
        return index 