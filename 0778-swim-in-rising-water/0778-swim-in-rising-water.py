class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time/elevation, row, col)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited[0][0] = True
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            # If we reached the destination, return the time (max elevation so far)
            if r == n-1 and c == n-1:
                return time
            
            # Explore 4-directionally adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))

        