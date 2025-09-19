class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral mapping
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse from right to left
        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value  # subtract if smaller before larger
            else:
                total += value  # otherwise add
            prev_value = value
        
        return total

        