class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Step 1: Sort potions for binary search
        potions.sort()
        m = len(potions)
        result = []

        # Step 2: For each spell, find how many potions form a successful pair
        for spell in spells:
            # Minimum potion strength needed for success
            min_potion = (success + spell - 1) // spell  # same as ceil(success / spell)
            
            # Binary search: find the first potion >= min_potion
            idx = bisect_left(potions, min_potion)
            
            # All potions from idx to end will form successful pairs
            result.append(m - idx)

        return result

        