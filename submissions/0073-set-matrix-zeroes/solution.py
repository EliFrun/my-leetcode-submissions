class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_rows = set()
        zero_columns = set()
        
        for i in enumerate(matrix):
            for j in enumerate(i[1]):
                if j[1] == 0:
                    zero_columns.add(j[0])
                    zero_rows.add(i[0])
                    
                    
                    
        for row in zero_rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
                
        for column in zero_columns:
            for i in range(len(matrix)):
                matrix[i][column] = 0
                

                    
