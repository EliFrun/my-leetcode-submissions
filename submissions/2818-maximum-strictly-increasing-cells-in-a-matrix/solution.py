class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        cells = [0] * (len(mat) * len(mat[0]))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cells[len(mat[0]) * i + j] = (mat[i][j], (i, j))

        cells.sort()
        
        r = [0] * len(mat)
        c = [0] * len(mat[0])
        ret = 0
        idx = 0
        while idx < len(cells):
            c_val, (i, j) = cells[idx]
            lis = [(i,j)]
            while idx < len(cells) and cells[idx][0] == c_val:
                lis.append(cells[idx][1])
                idx += 1

            b = defaultdict(int)
            for i, j in lis:
                b[(i,j)] = 1 + max(r[i], c[j])

            for (i,j), v in b.items():
                r[i] = max(r[i], v)
                c[j] = max(c[j], v)



        return max(r + c)



        
