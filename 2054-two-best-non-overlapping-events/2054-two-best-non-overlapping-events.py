class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import heapq
        
        # Sort events by start time
        events.sort()
        
        best_before = 0      # best value of finished events so far
        ans = 0
        heap = []            # (endTime, value)

        for start, end, value in events:
            # Pop all events that end BEFORE current event starts
            while heap and heap[0][0] < start:
                e_end, e_val = heapq.heappop(heap)
                best_before = max(best_before, e_val)

            # Option 1: combine current with best finished event
            ans = max(ans, best_before + value)

            # Option 2: maybe this single event is best
            ans = max(ans, value)

            # Push current event into heap
            heapq.heappush(heap, (end, value))

        return ans

        