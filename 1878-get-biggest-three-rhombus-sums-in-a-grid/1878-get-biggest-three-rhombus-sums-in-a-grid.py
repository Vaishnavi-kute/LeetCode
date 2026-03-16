class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):

                #size 0 rhombus
                s.add(grid[i][j])

                k = 1
                while True:
                    if i + 2*k >= m or j-k < 0 or j+k >= n:
                        break
                    total = 0

                    #top -> right
                    x, y = i, j
                    for d in range(k):
                        total += grid[x+d][y+d]

                    # right -> bottom 
                    x, y = i+k, j+k
                    for d in range(k):
                        total += grid[x+d][y-d]
                    
                    # bottom -> Left
                    x, y = i+2*k, j
                    for d in range(k):
                        total += grid[x-d][y-d]
                    
                    # Left -> top 
                    x, y = i+k, j-k
                    for d in range(k):
                        total += grid[x-d][y+d]
                    
                    s.add(total)
                    k += 1
        return   sorted(s, reverse=True)[:3]
        