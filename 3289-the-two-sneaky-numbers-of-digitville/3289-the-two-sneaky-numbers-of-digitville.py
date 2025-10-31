class Solution(object):
    def getSneakyNumbers(self, nums):
        seen = set()
        res = []

        for num in nums:
            if num in seen:
                res.append(num)
                if len(res) == 2:
                    return res
            else:
                seen.add(num)


        