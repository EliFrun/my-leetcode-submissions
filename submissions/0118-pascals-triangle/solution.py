class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]

        for i in range(1, numRows):
            prev = ret[-1]
            lis = [1]
            for j in range(len(prev)):
                lis.append(prev[j] + (prev[j + 1] if j + 1 < len(prev) else 0))
            ret.append(lis)
        return ret
        
