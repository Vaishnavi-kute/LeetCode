class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        total = 1 << k 
        
        # Early exit: not enough length to contain all codes
        if n < k + total - 1:
            return False
        
        seen = set()
        mask = 0
        
        for i in range(n):
            # Shift left and add current bit
            mask = ((mask << 1) & (total - 1)) | int(s[i])
            
            # Start recording once we have k bits
            if i >= k - 1:
                seen.add(mask)
                if len(seen) == total:
                    return True
        
        return False