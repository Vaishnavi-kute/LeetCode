class Router:

    def __init__(self, memoryLimit: int):
          self.memoryLimit = memoryLimit
          self.queue = deque()  # stores packets in FIFO order
          self.packetSet = set()  # to detect duplicates (source,destination,timestamp)
          self.destMap = defaultdict(list)  # destination -> sorted list of timestamps
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)

                # Check for duplicate
        if key in self.packetSet:
            return False

        # If at memory limit, remove oldest packet
        if len(self.queue) == self.memoryLimit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.packetSet.remove((old_source, old_dest, old_time))

            # Remove timestamp from destMap
            timestamps = self.destMap[old_dest]
            idx = bisect.bisect_left(timestamps, old_time)
            if idx < len(timestamps) and timestamps[idx] == old_time:
                timestamps.pop(idx)

        # Add new packet
        self.queue.append((source, destination, timestamp))
        self.packetSet.add(key)

        # Maintain sorted timestamps for this destination
        bisect.insort(self.destMap[destination], timestamp)

        return True
        

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        
        source, dest, time = self.queue.popleft()
        self.packetSet.remove((source, dest, time))

        # Remove from destMap
        timestamps = self.destMap[dest]
        idx = bisect.bisect_left(timestamps, time)
        if idx < len(timestamps) and timestamps[idx] == time:
            timestamps.pop(idx)

        return [source, dest, time]     

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0

        timestamps = self.destMap[destination]
        
        # Binary search for range [startTime, endTime]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left
        
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)