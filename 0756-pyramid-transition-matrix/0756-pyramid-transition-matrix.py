from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build map: (A,B) -> [C1, C2, ...]
        mp = defaultdict(list)
        for triplet in allowed:
            mp[(triplet[0], triplet[1])].append(triplet[2])
        
        memo = {}
        
        def dfs(row):
            # If only 1 block left, pyramid built
            if len(row) == 1:
                return True
            
            if row in memo:
                return memo[row]
            
            # Generate all possible next rows
            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs(path)
                
                pair = (row[i], row[i + 1])
                if pair not in mp:
                    return False
                
                for c in mp[pair]:
                    if build_next(i + 1, path + c):
                        return True
                return False
            
            memo[row] = build_next(0, "")
            return memo[row]
        
        return dfs(bottom)
