class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i + j >= len(matrix):
                    break
                if matrix[i + j][j] != matrix[i][0]:
                    return False
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if i + j >= len(matrix[0]):
                    break
                if matrix[j][i + j] != matrix[0][i]:
                    return False
        return True
        
