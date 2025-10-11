class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            # Base case: if we've formed a combination of the same length as digits
            if index == len(digits):
                res.append("".join(path))
                return

            # Get possible letters for the current digit
            for ch in phone_map[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()  # backtrack step

        backtrack(0, [])
        return res
        