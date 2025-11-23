class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 3 == 0:
            return total

        rem1 = sorted([x for x in nums if x % 3 == 1])
        rem2 = sorted([x for x in nums if x % 3 == 2])

        if total % 3 == 1:
            option1 = rem1[0] if rem1 else float('inf')
            option2 = rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf')
        else:
            option1 = rem2[0] if rem2 else float('inf')
            option2 = rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf')

        remove = min(option1, option2)

        return total - remove if remove != float('inf') else 0

        