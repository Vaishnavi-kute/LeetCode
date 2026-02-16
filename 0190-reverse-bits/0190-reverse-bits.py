class Solution:
    def reverseBits(self, n: int) -> int:
        if not hasattr(self, 'cache'):
            self.cache = {}
            for i in range(256):
                b = i
                rev = 0
                for _ in range(8):
                    rev = (rev << 1) | (b & 1)
                    b >>= 1
                self.cache[i] = rev

        return (
            self.cache[n & 0xff] << 24 |
            self.cache[(n >> 8) & 0xff] << 16 |
            self.cache[(n >> 16) & 0xff] << 8 |
            self.cache[(n >> 24) & 0xff]
        )     