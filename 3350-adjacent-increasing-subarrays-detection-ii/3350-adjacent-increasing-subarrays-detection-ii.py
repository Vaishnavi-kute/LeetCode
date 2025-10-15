class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        inc = [1] * n

        # Step 1: Compute length of increasing subarray ending at each index
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        ans = 0

        # Step 2: For each split point between two adjacent subarrays
        # We want two increasing subarrays: one ending at i, next starting at i+1
        # The possible k is min(inc[i], len of increasing subarray starting at i+1)
        # We'll compute the "start" version on the fly.

        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1

        # Step 3: Check adjacency boundary between i and i+1
        for i in range(n - 1):
            ans = max(ans, min(inc[i], right[i + 1]))

        return ans


