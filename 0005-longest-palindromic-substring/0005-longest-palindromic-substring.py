class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start, max_len = 0, 1

        def expandAroundCenter(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    start, max_len = left, curr_len
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd length palindrome
            expandAroundCenter(i, i)
            # Even length palindrome
            expandAroundCenter(i, i + 1)

        return s[start:start + max_len]

        