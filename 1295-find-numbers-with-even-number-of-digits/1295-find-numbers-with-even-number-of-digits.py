class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            # Convert number to string and check if length is even
            if len(str(num)) % 2 == 0:
                count += 1
        return count

        