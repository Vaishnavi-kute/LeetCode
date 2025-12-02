class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7

        from collections import defaultdict

        #Step 1: Count how many points lie on each horizontal live (same y)
        y_count = defaultdict(int)
        for x, y in points:
            y_count[y] += 1

        # Step 2:  for each pair of horizontal lines, calculate C(a,2) * C(b,2)
        ys = sorted(y_count.keys())
        c2 = lambda x: x * (x - 1) // 2 # nC2

        total = 0
        values = [y_count[y] for y in ys]

        # Pre- calc all C(n,2)
        combos = [c2(v) for v in values]

        #Steps 3: Sum combos[i] * combos[j] for all i < j
        prefix_sum = 0
        for c in combos :
            total = (total + c * prefix_sum) % MOD
            prefix_sum = (prefix_sum + c ) % MOD
        return total % MOD
        """
        :type points: List[List[int]]
        :rtype: int
        """
        