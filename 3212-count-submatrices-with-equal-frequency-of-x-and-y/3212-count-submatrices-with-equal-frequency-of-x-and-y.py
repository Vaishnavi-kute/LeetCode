class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        result = 0
        
        # prefix sums (we can optimize to O(1) space)
        prefix_sum = [[0]*n for _ in range(m)]
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                prefix_sum[i][j] = val
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    prefix_sum[i][j] += prefix_sum[i-1][j]
                    countX[i][j] += countX[i-1][j]
                
                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j-1]
                    countX[i][j] += countX[i][j-1]
                
                if i > 0 and j > 0:
                    prefix_sum[i][j] -= prefix_sum[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
                
                # check conditions
                if prefix_sum[i][j] == 0 and countX[i][j] > 0:
                    result += 1
        
        return result  