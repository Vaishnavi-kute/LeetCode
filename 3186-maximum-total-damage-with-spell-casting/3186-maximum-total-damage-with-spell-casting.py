class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from bisect import bisect_right
        from collections import Counter

        total = Counter(power)
        unique = sorted(total.keys())
        n = len(unique)
        dp = [0] * n

        for i in range(n):
            damage = unique[i] * total[unique[i]]
            j = bisect_right(unique, unique[i] - 3) - 1
            if j >= 0:
                damage += dp[j]
            dp[i] = max(dp[i-1] if i > 0 else 0, damage)

        return dp[-1]

        