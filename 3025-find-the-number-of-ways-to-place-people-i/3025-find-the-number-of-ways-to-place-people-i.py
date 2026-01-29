
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                
                # A must be upper-left of B
                if x1 <= x2 and y1 >= y2:
                    valid = True
                    
                    # Check if any other point lies inside or on the rectangle
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if x1 <= x <= x2 and y2 <= y <= y1:
                            valid = False
                            break
                    
                    if valid:
                        count += 1
        
        return count
