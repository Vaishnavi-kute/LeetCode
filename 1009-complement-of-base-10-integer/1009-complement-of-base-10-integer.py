class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        b = bin(n)[2:]          # binary string without '0b'
        comp = ""
        
        for bit in b:
            if bit == '0':
                comp += '1'
            else:
                comp += '0'
                
        return int(comp, 2)