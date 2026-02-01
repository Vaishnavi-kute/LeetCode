class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums_rest = nums[1:]
        nums_rest.sort()
        return nums[0] + nums_rest[0] + nums_rest[1]
