class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ret = copy.deepcopy(mat)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ret[i][j] = sum(
                    sum(
                        x[max(0, j - k):min(len(mat),j + k + 1)]
                    ) for x in mat[max(0, i - k):min(len(mat), i + k + 1)]
                )
                
        return ret
        
