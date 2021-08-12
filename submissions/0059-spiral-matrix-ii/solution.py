class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[-1] * n for i in range(n)]
        k = 1
        for i in range(n // 2 + 1):
            for j in range(i, n - i):
                ret[i][j] = k
                k += 1

            for j in range(i + 1, n - i):
                ret[j][n - 1 - i] = k
                k += 1

            for j in range(n - 2 - i, i - 1, -1):
                ret[n - 1 - i][j] = k
                k += 1

            for j in range(n - 2 - i, i, - 1):
                ret[j][i] = k
                k += 1  
        return ret
