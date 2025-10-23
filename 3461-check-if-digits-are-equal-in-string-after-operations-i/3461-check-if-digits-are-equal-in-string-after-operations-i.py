class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert string to list of integers
        digits = [int(ch) for ch in s]

        # Repeat until only 2 digits remain
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits

        # Check if both digits are equal
        return digits[0] == digits[1]

        