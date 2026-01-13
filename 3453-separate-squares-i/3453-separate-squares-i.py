class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y = 0
        
        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        
        half = total_area / 2.0
        
        def area_below(Y):
            area = 0.0
            for _, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += l * (Y - y)
            return area
        
        low, high = min_y, max_y
        
        for _ in range(60):  # sufficient for 1e-5 precision
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid
        
        return low
        