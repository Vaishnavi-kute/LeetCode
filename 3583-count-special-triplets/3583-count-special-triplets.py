class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        from collections import Counter
        
        rightCount = Counter(nums)   # all elements initially on the right
        leftCount = Counter()        # empty initially
        
        ans = 0
        
        for j in range(len(nums)):
            rightCount[nums[j]] -= 1   # nums[j] is no longer on right
            
            target = nums[j] * 2       # nums[i] and nums[k] must equal this
            
            if target in leftCount and target in rightCount:
                ans = (ans + leftCount[target] * rightCount[target]) % MOD
            
            leftCount[nums[j]] += 1    # nums[j] now becomes part of left
        
        return ans

        