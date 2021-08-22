class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ret = [[1], [1,1]]
        for i in range(2, numRows):
            lis = [0] * (i + 1)
            lis[0] = 1
            lis[-1] = 1
            
            for j in range(1, i):
                lis[j] = ret[i - 1][j - 1] + ret[i - 1][j]
                
            ret.append(lis)
            
        return ret
