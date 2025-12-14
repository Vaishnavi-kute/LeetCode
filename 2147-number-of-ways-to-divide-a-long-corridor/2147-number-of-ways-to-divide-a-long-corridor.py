class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # Count total seats
        total_seats = corridor.count('S')
        
        # If seats are odd or less than 2, impossible
        if total_seats < 2 or total_seats % 2 != 0:
            return 0
        
        ways = 1
        seat_count = 0
        plants_between = 0
        in_gap = False
        
        for c in corridor:
            if c == 'S':
                seat_count += 1
                if seat_count % 2 == 0:
                    # End of a pair
                    in_gap = True
                elif in_gap:
                    # Start of next pair
                    ways = (ways * (plants_between + 1)) % MOD
                    plants_between = 0
                    in_gap = False
            elif in_gap:
                plants_between += 1
        
        return ways

        