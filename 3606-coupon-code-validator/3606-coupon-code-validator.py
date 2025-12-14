class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]: 
        # Allowed business lines in required order
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            # Check isActive
            if not active:
                continue
            
            # Check valid business line
            if b not in order:
                continue
            
            # Check valid code (non-empty, alphanumeric or underscore)
            if not c or not re.match(r'^[A-Za-z0-9_]+$', c):
                continue
            
            valid_coupons.append((order[b], c))
        
        # Sort by business line order, then by code lexicographically
        valid_coupons.sort()
        
        # Extract only codes
        return [c for _, c in valid_coupons]

        