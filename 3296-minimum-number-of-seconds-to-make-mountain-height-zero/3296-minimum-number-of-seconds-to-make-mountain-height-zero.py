class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        left = 0
        right = 10**18

        while left < right:
            mid = (left + right) // 2
            total_height = 0

            for t in workerTimes:
                val = (2 * mid) // t
                x = int((math.sqrt(1 + 4 * val) - 1) // 2)
                total_height += x

            if total_height >= mountainHeight:
                right = mid
            else:
                left = mid + 1

        return left
        