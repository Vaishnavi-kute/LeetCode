class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        m, n = len(coins), len(coins[0])

        NEG_INF = float('-inf')

        # dp[i][j][k]
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        # Initialize start
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0  # neutralize

        for i in range(m):
            for j in range(n):
                for k in range(3):

                    if dp[i][j][k] == NEG_INF:
                        continue

                    # Move Right
                    if j + 1 < n:
                        val = coins[i][j + 1]

                        if val >= 0:
                            dp[i][j + 1][k] = max(
                                dp[i][j + 1][k],
                                dp[i][j][k] + val
                            )
                        else:
                            # take loss
                            dp[i][j + 1][k] = max(
                                dp[i][j + 1][k],
                                dp[i][j][k] + val
                            )

                            # neutralize
                            if k < 2:
                                dp[i][j + 1][k + 1] = max(
                                    dp[i][j + 1][k + 1],
                                    dp[i][j][k]
                                )

                    # Move Down
                    if i + 1 < m:
                        val = coins[i + 1][j]

                        if val >= 0:
                            dp[i + 1][j][k] = max(
                                dp[i + 1][j][k],
                                dp[i][j][k] + val
                            )
                        else:
                            # take loss
                            dp[i + 1][j][k] = max(
                                dp[i + 1][j][k],
                                dp[i][j][k] + val
                            )

                            # neutralize
                            if k < 2:
                                dp[i + 1][j][k + 1] = max(
                                    dp[i + 1][j][k + 1],
                                    dp[i][j][k]
                                )

        return max(dp[m - 1][n - 1])