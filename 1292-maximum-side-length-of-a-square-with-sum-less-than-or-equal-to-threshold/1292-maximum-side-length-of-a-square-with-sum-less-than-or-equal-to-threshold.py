class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )
        
        # Function to check if a square of side k exists
        def is_valid(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    square_sum = (
                        prefix[i][j]
                        - prefix[i - k][j]
                        - prefix[i][j - k]
                        + prefix[i - k][j - k]
                    )
                    if square_sum <= threshold:
                        return True
            return False
        
        # Binary search for maximum side length
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid
            else:
                right = mid - 1
        
        return left

        