class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] = number of paths reaching column j with remainder r
        dp = [[0] * k for _ in range(n)]

        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                val_mod = grid[i][j] % k

                # From top (use dp[j])
                if i > 0:
                    for r in range(k):
                        nr = (r + val_mod) % k
                        new_dp[j][nr] = (new_dp[j][nr] + dp[j][r]) % MOD

                # From left (use new_dp[j-1])
                if j > 0:
                    for r in range(k):
                        nr = (r + val_mod) % k
                        new_dp[j][nr] = (new_dp[j][nr] + new_dp[j-1][r]) % MOD

                # Starting cell (0,0)
                if i == 0 and j == 0:
                    new_dp[0][val_mod] = 1

            dp = new_dp  # Move to next row

        return dp[n-1][0]
