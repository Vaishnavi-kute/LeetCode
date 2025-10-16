

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        count = Counter([(num % value + value) % value for num in nums])
        for i in range(len(nums)):
            if count[i % value] == 0:
                return i
            count[i % value] -= 1
        return len(nums)
       