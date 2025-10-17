class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def count(s):
            freq, distinct, parts = [0]*26, 0, 0
            for ch in s:
                idx = ord(ch)-97
                if freq[idx] == 0: distinct += 1
                freq[idx] += 1
                if distinct > k:
                    parts += 1
                    freq = [0]*26
                    freq[idx] = 1
                    distinct = 1
            return parts + 1

        ans = count(s)
        for i, ch in enumerate(s):
            for c in map(chr, range(97, 123)):
                if c != ch:
                    ans = max(ans, count(s[:i]+c+s[i+1:]))
        return ans
