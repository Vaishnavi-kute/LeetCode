from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        # Check triangle inequality
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        # All sides equal
        if a == b == c:
            return "equilateral"

        # Two sides equal
        if a == b or b == c or a == c:
            return "isosceles"

        # All different
        return "scalene"

        