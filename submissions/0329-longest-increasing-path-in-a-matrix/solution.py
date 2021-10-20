class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = [[None] * len(matrix[0]) for i in range(len(matrix))]
        
        def dfs(i, j):
            if cache[i][j]:
                return cache[i][j]
            
            ret = 1
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                ret = max(ret, 1 + dfs(i - 1, j))
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                ret = max(ret, 1 + dfs(i, j - 1))
            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                ret = max(ret, 1 + dfs(i + 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                ret = max(ret, 1 + dfs(i, j + 1))
            
            cache[i][j] = ret
            return ret
        
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret = max(ret, dfs(i, j))
                
        return ret
        
            
            
