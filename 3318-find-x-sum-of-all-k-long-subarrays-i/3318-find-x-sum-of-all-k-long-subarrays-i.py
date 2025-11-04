class Solution(object):
    def findXSum(self, nums, k, x):
                
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            window = nums[i : i + k]
            
            # Frequency map
            freq = Counter(window)
            
            # Sort by: frequency desc, value desc
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            total = 0
            chosen = 0
            
            for val, cnt in sorted_items:
                if chosen == x:
                    break
                total += val * cnt
                chosen += 1
            
            ans.append(total)
        
        return ans
   