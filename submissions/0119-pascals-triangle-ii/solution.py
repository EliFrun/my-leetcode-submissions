class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ret = [1,1]
        for i in range(2, rowIndex + 1):
            lis = [0] * (i + 1)
            lis[0] = 1
            lis[-1] = 1
            
            for j in range(1, i):
                lis[j] = ret[j - 1] + ret[j]
                
            ret = lis
            
        return ret
        
