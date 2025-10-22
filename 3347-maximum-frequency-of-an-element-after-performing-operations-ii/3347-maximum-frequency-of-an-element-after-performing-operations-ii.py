from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        res = 1

        for right in range(n):
            # shrink the window if the difference is too large
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # total elements in window
            window_size = right - left + 1
            # we can modify at most numOperations elements
            res = max(res, min(window_size, numOperations + 1))

        return res

        