class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}             # lake -> last day it was full
        dry_days = SortedList()  # indices of dry days (0 days)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(i)   # mark this as a day we can use to dry
                ans[i] = 1        # default value (may change later)
            else:
                if lake in full:
                    # find a dry day after the lake was last filled
                    idx = dry_days.bisect_right(full[lake])
                    if idx == len(dry_days):
                        return []   # no available dry day → flood
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  # dry this lake on that day
                    dry_days.remove(dry_day)
                
                full[lake] = i  # mark this lake as now full
                
        return ans

        