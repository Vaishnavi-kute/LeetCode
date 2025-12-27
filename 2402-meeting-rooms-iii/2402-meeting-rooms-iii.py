class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()

        # Min-heap of available room numbers
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of (end_time, room)
        busy = []

        # Count meetings per room
        count = [0] * n

        for start, end in meetings:
            # Free up any rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                finish_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                # Assign to the smallest-index available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # No room available — delay the meeting
                finish_time, room = heapq.heappop(busy)
                new_end = finish_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # Return room with maximum meetings (smallest index if tie)
        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i

