class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        for i in range(min(len(matrix), len(matrix[0]))):
            if len(ret) == len(matrix) * len(matrix[0]):
                break
            for j in range(i, len(matrix[0]) - i):
                ret += [matrix[i][j]]    
            if len(ret) == len(matrix) * len(matrix[0]):
                break
            
            for j in range(i + 1, len(matrix) - i):
                ret += [matrix[j][len(matrix[0]) - 1 - i]]  
            if len(ret) == len(matrix) * len(matrix[0]):
                break
            
            for j in range(len(matrix[0]) - 2 - i, i - 1, -1):
                ret += [matrix[len(matrix) - 1 - i][j]] 
            if len(ret) == len(matrix) * len(matrix[0]):
                break
            
            for j in range(len(matrix) - 2 - i, i, - 1):
                ret += [matrix[j][i]] 
            if len(ret) == len(matrix) * len(matrix[0]):
                break
            
        return ret
