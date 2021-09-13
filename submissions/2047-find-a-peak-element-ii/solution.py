class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                above, below, left, right = (
                    mat[i - 1][j] if i > 0 else -1,
                    mat[i + 1][j] if i < len(mat) - 1 else -1,
                    mat[i][j - 1] if j > 0 else -1,
                    mat[i][j + 1] if j < len(mat[0]) - 1 else -1
                )
                
                if val > max(above, below, left, right):
                    return [i, j]
