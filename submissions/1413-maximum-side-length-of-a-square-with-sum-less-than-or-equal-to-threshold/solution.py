class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]
        ret = 0
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        start = [(0, x) for x in range(len(mat[0]))] + [(x, 0) for x in range(1, len(mat))]
        ret = 0
        for i, j in start:
            left = 0
            k = ret
            s = 0
            while i + k < len(prefix) and j + k < len(prefix[0]):
                s = prefix[i + k][j + k] - prefix[i + left][j + k] - prefix[i + k][j + left] + prefix[i + left][j + left]
                while s > threshold:
                    left += 1
                    s = prefix[i + k][j + k] - prefix[i + left][j + k] - prefix[i + k][j + left] + prefix[i + left][j + left]
                if k - left > ret:
                    ret = k - left
                k += 1
        return max(0, ret)
                
        
        
