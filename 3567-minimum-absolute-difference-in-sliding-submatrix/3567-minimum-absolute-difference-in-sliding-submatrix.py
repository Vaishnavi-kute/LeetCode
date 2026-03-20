class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = set()  # use set for distinct values

                # collect elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])

                vals = sorted(vals)

                # if only one distinct value → answer = 0
                if len(vals) <= 1:
                    row.append(0)
                    continue

                # find min difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])

                row.append(min_diff)

            ans.append(row)

        return ans
