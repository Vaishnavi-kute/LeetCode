class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        import math
        
        n = len(nums)
        prefix = 0
        
        # min_prefix_mod[r] = smallest prefix sum seen at index % k == r
        min_prefix_mod = [math.inf] * k
        min_prefix_mod[0] = 0  # prefix before starting
        
        ans = -10**30  # Very small number
        
        for i, x in enumerate(nums, 1):
            prefix += x
            r = i % k
            
            # candidate subarray ending here
            ans = max(ans, prefix - min_prefix_mod[r])
            
            # update minimum prefix for this remainder bucket
            min_prefix_mod[r] = min(min_prefix_mod[r], prefix)
        
        return ans

        