class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #Function to rotate matrix 90 degrees clockwise
        
        # Function to rotate matrix 90 degrees clockwise
        def rotate(matrix):
            # Transpose
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Reverse each row
            for row in matrix:
                row.reverse()
        
        # Try all 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False