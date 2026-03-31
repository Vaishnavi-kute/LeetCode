class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0] * 26
        odd = [0] * 26

        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')

            if i % 2 == 0:
                even[idx1] += 1
                even[idx2] -= 1
            else:
                odd[idx1] += 1
                odd[idx2] -= 1

        return even == [0] * 26 and odd == [0] * 26