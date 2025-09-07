
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        n, m = len(word1), len(word2)

        # Merge characters alternately
        while i < n and j < m:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        if i < n:
            result.append(word1[i:])
        if j < m:
            result.append(word2[j:])

        return "".join(result)
        