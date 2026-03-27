class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        shift = k % n

        for i in range(m):
            row = mat[i]

            if i % 2 == 0:
                # left shift
                shifted = row[shift:] + row[:shift]
            else:
                # right shift
                shifted = row[-shift:] + row[:-shift]

            if shifted != row:
                return False

        return True