class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        count = 0
        
        # partition index i goes from 0 to n-2
        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left
            
            if (left % 2) == (right % 2):
                count += 1
        
        return count
        