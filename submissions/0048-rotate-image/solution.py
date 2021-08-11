class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        layers = (len(matrix) + 1) // 2
        
        for y in range(layers): 
            for x in range(0, len(matrix) - 1 - 2 * y):
                corners = [
                    [y + x,  len(matrix) - 1 - y], # top right
                    [len(matrix) - 1 - y, len(matrix) - 1 - y - x], # bottom right
                    [len(matrix) - 1 - y - x, y], # bottom left
                    [y, y  + x] # top left
                ]
                save = matrix[y][y + x]
                for corner in corners:
                    current = save
                    save = matrix[corner[0]][corner[1]]
                    matrix[corner[0]][corner[1]] = current
    
    
