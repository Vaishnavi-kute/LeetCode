from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # nums[0] is always included
        base = nums[0]
        need = k - 1

        # Two heaps
        small = []  # max heap (store negative values)
        large = []  # min heap
        small_sum = 0

        def add(x):
            nonlocal small_sum
            if len(small) < need:
                heappush(small, -x)
                small_sum += x
            else:
                if -small[0] > x:
                    moved = -heappop(small)
                    small_sum -= moved
                    heappush(large, moved)
                    heappush(small, -x)
                    small_sum += x
                else:
                    heappush(large, x)

        def remove(x):
            nonlocal small_sum
            if x <= -small[0]:
                small.remove(-x)
                small_sum -= x
                heapq.heapify(small)
                if large:
                    moved = heappop(large)
                    heappush(small, -moved)
                    small_sum += moved
            else:
                large.remove(x)
                heapq.heapify(large)

        # Initial window
        for i in range(1, dist + 2):
            add(nums[i])

        ans = small_sum

        # Slide window
        for i in range(dist + 2, len(nums)):
            add(nums[i])
            remove(nums[i - (dist + 1)])
            ans = min(ans, small_sum)

        return base + ans
