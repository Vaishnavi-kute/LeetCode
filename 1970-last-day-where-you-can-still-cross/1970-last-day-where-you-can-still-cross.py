class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        
        parent = list(range(n + 2))
        size = [1] * (n + 2)
        
        TOP = n
        BOT = n + 1
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]
        
        grid = [[0] * col for _ in range(row)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # process in reverse: from last day to first
        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1
            grid[r][c] = 1  # make land
            
            idx = r * col + c
            
            if r == 0:
                union(idx, TOP)
            if r == row - 1:
                union(idx, BOT)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union(idx, nr * col + nc)
            
            if find(TOP) == find(BOT):
                return i  # i is the last day you can still cross
