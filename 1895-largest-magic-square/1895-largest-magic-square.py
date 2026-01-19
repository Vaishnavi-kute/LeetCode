class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Row and column prefix sums
        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]

        # Diagonal prefix sums
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]  # main diagonal
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]  # anti-diagonal

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        # Try largest square first
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_ps[i][j + k] - row_ps[i][j]

                    # Check rows
                    if any(row_ps[i + r][j + k] - row_ps[i + r][j] != target for r in range(k)):
                        continue

                    # Check columns
                    if any(col_ps[i + k][j + c] - col_ps[i][j + c] != target for c in range(k)):
                        continue

                    # Check diagonals
                    d1 = diag1[i + k][j + k] - diag1[i][j]
                    d2 = diag2[i + k][j] - diag2[i][j + k]
                    if d1 != target or d2 != target:
                        continue

                    return k

        return 1
