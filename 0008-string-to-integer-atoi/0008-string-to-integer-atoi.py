class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Remove leading whitespace
        if not s:
            return 0

        # 2. Determine sign
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1

        # 3. Read digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # 4. Apply sign
        num *= sign

        # 5. Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

        