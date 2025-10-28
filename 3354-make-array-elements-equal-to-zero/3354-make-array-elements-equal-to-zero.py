class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        def simulate(start, direction):
            arr = nums[:]  # make a copy
            curr = start
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction
                else:
                    arr[curr] -= 1
                    direction *= -1
                    curr += direction
            return all(x == 0 for x in arr)

        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):   # try moving right
                    ans += 1
                if simulate(i, -1):  # try moving left
                    ans += 1
        return ans
       