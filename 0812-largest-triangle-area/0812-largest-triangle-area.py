class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            # Using the shoelace formula for triangle area
            return abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            ) / 2
        
        n = len(points)
        max_area = 0.0
        
        # Try all combinations of 3 points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, area(points[i], points[j], points[k]))
        
        return max_area

        