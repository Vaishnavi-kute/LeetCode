class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty = 0
        
        # Drink all initial bottles
        total_drunk += numBottles
        empty += numBottles
        
        # Continue exchanging as long as possible
        while empty >= numExchange:
            # Exchange empty bottles for one full bottle
            empty -= numExchange
            numExchange += 1  # exchange cost increases
            total_drunk += 1  # drink the new bottle
            empty += 1        # becomes empty again after drinking
            
        return total_drunk

        