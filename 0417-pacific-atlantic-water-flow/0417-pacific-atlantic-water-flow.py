class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols 
                    and not visited[nr][nc] 
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        # Start from Pacific border (top row + left col)
        for c in range(cols):
            dfs(0, c, pacific)           # top
            dfs(rows - 1, c, atlantic)   # bottom
        
        for r in range(rows):
            dfs(r, 0, pacific)           # left
            dfs(r, cols - 1, atlantic)   # right
        
        # Collect cells that can reach both
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result

        