class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n= len(matrix), len(matrix[0])

        #step 1 : Build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0

        #Step 2: Process each row
        for row in matrix:
            #Sort in descending order 
            row.sort(reverse = True)

            # Step 3: Calculate max area
            for j in range(n):
                area = row[j] * (j + 1)
                max_area = max(max_area, area)

        return max_area


        
        