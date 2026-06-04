class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            s = str(num)
            n = len(s)

            if n < 3:
                return 0

            count = 0
            for i in range(1, n - 1):
                left = int(s[i - 1])
                mid = int(s[i])
                right = int(s[i + 1])

                # Peak
                if mid > left and mid > right:
                    count += 1
                # Valley
                elif mid < left and mid < right:
                    count += 1

            return count

        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)

        return total