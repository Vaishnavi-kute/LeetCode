
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and handle carry
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, done
            digits[i] = 0  # Set to 0 and continue (carry over)
        
        # If all digits were 9 (e.g., 999 -> 1000)
        return [1] + digits

        