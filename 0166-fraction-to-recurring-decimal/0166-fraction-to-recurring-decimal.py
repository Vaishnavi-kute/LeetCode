class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle negative result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with positive values
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)  # No fractional part

        result.append(".")

        # Fractional part
        remainder_map = {}  # remainder -> position in result
        while remainder:
            if remainder in remainder_map:
                # Repeating remainder found
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)

        