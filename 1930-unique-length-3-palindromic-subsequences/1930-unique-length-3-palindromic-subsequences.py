class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        n = len(s)

        for ch in set(s):
            l = s.find(ch)
            r = s.rfind(ch)
            if l < r:
                # unique characters between l and r
                res += len(set(s[l+1:r]))

        return res
        