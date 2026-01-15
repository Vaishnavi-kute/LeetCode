class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        countZero = 0
        result = 0
        
        for num in nums:
            if num == 0:
                countZero += 1
                result += countZero
            else:
                countZero = 0
                
        return result

        