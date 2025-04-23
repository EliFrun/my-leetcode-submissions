class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] for _ in  range(len(matrix))]
        for i,l in enumerate(self.prefix):
            for x in matrix[i]:
                l.append(l[-1] + x)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = 0
        for i in range(row1, row2 + 1):
            ret += self.prefix[i][col2 + 1] - self.prefix[i][col1]
        return ret
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
