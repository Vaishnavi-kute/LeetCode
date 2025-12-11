from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # track min and max y for each row x, and min and max x for each column y
        row_min = defaultdict(lambda: float('inf'))
        row_max = defaultdict(lambda: -float('inf'))
        col_min = defaultdict(lambda: float('inf'))
        col_max = defaultdict(lambda: -float('inf'))
        
        for x, y in buildings:
            if y < row_min[x]: row_min[x] = y
            if y > row_max[x]: row_max[x] = y
            if x < col_min[y]: col_min[y] = x
            if x > col_max[y]: col_max[y] = x
        
        covered = 0
        for x, y in buildings:
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                covered += 1
        
        return covered


        