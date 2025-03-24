class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix = [[0] for _ in range(len(mat))]
        ret = 0
        for i, row in enumerate(mat):
            for v in row:
                prefix[i].append(prefix[i][-1] + v)

        def solve(i, j, k):
            square_sum = 0
            for l in range(k + 1):
                square_sum += prefix[i + l][j + k + 1] - prefix[i + l][j]
            return square_sum
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                bottom, top = 0, min(len(mat[0]) - j, len(mat) - i) - 1
                while top - bottom > 1:
                    k = (bottom + top) // 2

                    if solve(i,j,k) <= threshold:
                        bottom = k
                    else:
                        top = k
                if solve(i,j,top) <= threshold:
                    ret = max(ret, top + 1)
                elif solve(i,j,bottom) <= threshold:
                    ret = max(ret, bottom + 1)
        return ret
        
