class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        number_of_negatives = 0
        minimum = 100001
        ret = 0
        for row in matrix:
            for val in row:
                ret += abs(val)
                if val < 0:
                    number_of_negatives += 1
                minimum = min(minimum, abs(val))
                
        if number_of_negatives % 2 == 1:
            ret -= 2 * minimum
        
        return ret
        
