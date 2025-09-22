class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = last_max = -1
        last_invalid = -1
        res = 0

        for i, num in enumerate(nums):
            # If num is out of range, reset window
            if num < minK or num > maxK:
                last_invalid = i
            
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i

            # Count valid subarrays ending at i
            res += max(0, min(last_min, last_max) - last_invalid)

        return res

        