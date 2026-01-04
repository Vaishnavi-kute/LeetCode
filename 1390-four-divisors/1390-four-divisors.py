class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for n in nums:
            divs = set()
            
            # count divisors up to sqrt(n)
            for d in range(1, int(n ** 0.5) + 1):
                if n % d == 0:
                    divs.add(d)
                    divs.add(n // d)
                    
                    # if more than 4, no need to continue
                    if len(divs) > 4:
                        break
            
            if len(divs) == 4:
                ans += sum(divs)
        
        return ans

     