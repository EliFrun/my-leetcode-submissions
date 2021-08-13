class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower, upper = 0, len(matrix) - 1
        
        while upper - lower > 1:
            mid = (upper + lower) // 2
            
            if matrix[mid][0] > target:
                upper = mid
                
            else:
                lower = mid
          
        if target < matrix[upper][0] and target > matrix[lower][-1]:
            return False
        
        index = upper if target >= matrix[upper][0] else lower
        lower, upper = 0, len(matrix[index]) - 1
        
        while upper - lower > 1:
            mid = (upper + lower) // 2
            
            if matrix[index][mid] > target:
                upper = mid
                
            else:
                lower = mid
                
                
        return matrix[index][lower] == target or matrix[index][upper] == target
