class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        # Subtract using bit shifts
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double temp until it would exceed dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        # Apply sign
        if negative:
            result = -result
        
        # Clamp to 32-bit integer range
        return max(INT_MIN, min(INT_MAX, result))
