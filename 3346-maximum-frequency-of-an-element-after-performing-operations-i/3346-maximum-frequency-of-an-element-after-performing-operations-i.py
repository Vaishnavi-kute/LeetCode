class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        ans = 1

        for right in range(n):
            # shrink the window if nums[right] - nums[left] > 2*k
            while nums[right] - nums[left] > 2 * k:
                left += 1

            # window size = right - left + 1
            # we can change at most numOperations elements
            curr_window = right - left + 1
            ans = max(ans, min(curr_window, numOperations + 1))

        return ans
