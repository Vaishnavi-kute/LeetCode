class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        
        for i, jump in enumerate(nums):
            if i > reachable:   # cannot move further
                return False
            reachable = max(reachable, i + jump)
            
            if reachable >= len(nums) - 1:
                return True
        
        return True