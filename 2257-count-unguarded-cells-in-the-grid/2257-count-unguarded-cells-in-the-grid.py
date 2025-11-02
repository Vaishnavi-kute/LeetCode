class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]

        # mark guards as 1, walls as 2
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        # function to mark in one direction
        def mark(r, c, dr, dc):
            nr, nc = r + dr, c + dc
            while 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == 2 or grid[nr][nc] == 1: 
                    break  # wall or another guard
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 3  # mark as guarded
                nr += dr
                nc += dc

        # directions -> up, down, left, right
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        # for each guard, mark all 4 directions
        for r, c in guards:
            for dr, dc in dirs:
                mark(r, c, dr, dc)

        # count unguarded & empty cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        return count
