class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count odds in range [low, high]
        # Formula: (high + 1) // 2 - low // 2
        return (high + 1) // 2 - low // 2
        