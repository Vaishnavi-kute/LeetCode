class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
  # Sort by the end ascending, and if tie by start descending
        intervals.sort(key = lambda x: (x[1], - x[0]))

        # p1 and p2 represent last two chosen points
        p1 = -1
        p2 = -1
        ans = 0

        for l, r in intervals:
            #Case 1: interval alresady contains p1 and p2 
            if l <= p1:
                continue

            #Case 2: interval contains only p2 add one new number r
            elif l <= p2:
                ans += 1
                p1, p2 = p2, r

            else:
                ans += 2
                p1, p2 = r - 1, r
        return ans


        