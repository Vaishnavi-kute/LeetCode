from typing import List
MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)

        # Precompute factorials and modular inverses
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        # Precompute nums[i]^c for c = 0..m
        pow_num = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            a = nums[i] % MOD
            for c in range(1, m + 1):
                pow_num[i][c] = pow_num[i][c - 1] * a % MOD

        # dp[(t, carry, ones)] = accumulated contribution
        dp = {(0, 0, 0): 1}

        for i in range(n):
            new_dp = {}
            for (t, carry, ones), val in dp.items():
                maxc = m - t
                for c in range(maxc + 1):
                    new_t = t + c
                    total = carry + c
                    bit = total & 1
                    new_carry = total >> 1
                    new_ones = ones + bit
                    if new_ones > m:
                        continue
                    add = val * pow_num[i][c] % MOD * inv_fact[c] % MOD
                    key = (new_t, new_carry, new_ones)
                    new_dp[key] = (new_dp.get(key, 0) + add) % MOD
            dp = new_dp

        # Final answer: sum over states with t == m and popcount(carry)+ones == k
        ans = 0
        for (t, carry, ones), val in dp.items():
            if t != m:
                continue
            total_ones = ones + carry.bit_count()
            if total_ones == k:
                ans = (ans + val * fact[m]) % MOD

        return ans % MOD
