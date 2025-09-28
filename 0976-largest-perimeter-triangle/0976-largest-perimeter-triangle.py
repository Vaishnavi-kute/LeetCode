class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort in descending order
        nums.sort(reverse=True)
        
        # Check triplets from largest to smallest
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:  # Triangle condition
                return a + b + c
        
        return 0  # No valid triangle found

        