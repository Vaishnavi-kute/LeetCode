class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        s = "1"
        for _ in range(n - 1):
            new_s = ""
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    new_s += str(count) + s[i - 1]
                    count = 1
            new_s += str(count) + s[-1]  # Add the last group
            s = new_s
        return s
