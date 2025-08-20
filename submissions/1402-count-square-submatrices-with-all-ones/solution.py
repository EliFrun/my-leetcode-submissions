class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        curr = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr[j] = curr[j] + 1 if matrix[i][j] == 1 else 0
                
                min_sq = curr[j]
                # can we make a square of size k + 1
                for k in range(curr[j] + 1):
                    if j - k < 0:
                        k -= 1
                        break
                    # all values must be larger than k + 1
                    min_sq = min(min_sq, curr[j - k])
                    if min_sq < k + 1:
                        k -= 1
                        break
                ret += k + 1
        return ret

            
        
