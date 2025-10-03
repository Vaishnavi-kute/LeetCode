import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # (height, row, col)
        
        # 1️⃣ Push all boundary cells into heap
        for r in range(m):
            for c in range(n):
                if r in (0, m-1) or c in (0, n-1):
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        
        # 2️⃣ Directions (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        water_trapped = 0
        
        # 3️⃣ Process cells from lowest boundary
        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # If neighbor is lower, water is trapped
                    water_trapped += max(0, height - heightMap[nr][nc])
                    # Push the higher of water level or cell height
                    heapq.heappush(heap, (max(heightMap[nr][nc], height), nr, nc))
        
        return water_trapped

        