from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * n
        prefix = [0] * (n + 1)   # prefix[i] = sum(dp[0..i-1])

        maxdq = deque()
        mindq = deque()

        left = 0

        for i in range(n):

            # Maintain max deque
            while maxdq and nums[maxdq[-1]] <= nums[i]:
                maxdq.pop()
            maxdq.append(i)

            # Maintain min deque
            while mindq and nums[mindq[-1]] >= nums[i]:
                mindq.pop()
            mindq.append(i)

            # Shrink window until max - min <= k
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                left += 1
                if maxdq[0] < left:
                    maxdq.popleft()
                if mindq[0] < left:
                    mindq.popleft()

            # Now valid window is [left ... i]

            # dp[i] = sum of dp[left-1 ... i-1]
            if left == 0:
                # sum dp[-1]...dp[i-1] = prefix[i] + 1
                dp[i] = (prefix[i] + 1) % MOD
            else:
                dp[i] = (prefix[i] - prefix[left - 1]) % MOD

            prefix[i + 1] = (prefix[i] + dp[i]) % MOD

        return dp[-1] % MOD
