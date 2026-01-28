class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        # Min-heap: (cost, i, j, teleports_used)
        pq = [(0, 0, 0, 0)]
        
        # Pre-store all cells sorted by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        while pq:
            cost, i, j, t = heappop(pq)
            
            if cost > dist[i][j][t]:
                continue
            
            # Reached destination
            if i == m - 1 and j == n - 1:
                return cost
            
            # Normal moves: right & down
            for ni, nj in [(i, j + 1), (i + 1, j)]:
                if ni < m and nj < n:
                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][t]:
                        dist[ni][nj][t] = new_cost
                        heappush(pq, (new_cost, ni, nj, t))
            
            # Teleportation
            if t < k:
                curr_val = grid[i][j]
                for val, x, y in cells:
                    if val > curr_val:
                        break
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heappush(pq, (cost, x, y, t + 1))
        
        return -1

        