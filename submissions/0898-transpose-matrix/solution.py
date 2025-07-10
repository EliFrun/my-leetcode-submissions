class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = []
        for j in range(len(matrix[0])):
            lis = []
            for i in range(len(matrix)):
                lis.append(matrix[i][j])
            ret.append(lis)

        return ret
        
