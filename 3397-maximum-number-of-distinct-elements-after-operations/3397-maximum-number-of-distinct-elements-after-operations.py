class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used = set()
        res = 0

        for x in nums:
            for val in range(x - k, x + k + 1):
                if val not in used:
                    used.add(val)
                    res += 1
                    break
        return res