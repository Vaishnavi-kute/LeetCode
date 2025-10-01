class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles  # start with all full bottles
        empty = numBottles        # all become empty after drinking
        
        while empty >= numExchange:
            new_full = empty // numExchange        # exchange empty bottles for new full ones
            total_drunk += new_full                # drink those new bottles
            empty = empty % numExchange + new_full # remaining empty + new empties
        
        return total_drunk
       