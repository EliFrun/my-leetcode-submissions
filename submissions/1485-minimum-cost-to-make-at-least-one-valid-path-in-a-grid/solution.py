class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        costs = [[ -1 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        curr = set([(0,0)])
        layer = 0
        while curr:
            nxt = set()
            for i,j in curr:
                curr_idx = (i, j)
                while curr_idx:
                    i, j = curr_idx
                    costs[i][j] = layer
                    if i == len(grid) - 1 and j == len(grid[0]) - 1:
                        return layer
                    lis = [(0, 1), (0, -1), (1,0), (-1,0)]
                    di, dj = lis[grid[i][j] - 1]
                    lis.pop(grid[i][j] - 1)
                    for dbi, dbj in lis:
                        if (i + dbi >= 0 and
                            i + dbi < len(grid) and 
                            j + dbj >= 0 and
                            j + dbj < len(grid[0]) and
                            costs[i + dbi][j + dbj] == -1
                        ):
                            nxt.add((i + dbi, j + dbj))
                    if (i + di >= 0 and
                        i + di < len(grid) and 
                        j + dj >= 0 and
                        j + dj < len(grid[0]) and
                        costs[i + di][j + dj] == -1
                    ):
                        curr_idx = (i + di, j + dj)
                    else:
                        curr_idx = None

            curr = nxt
            layer += 1

        return 0

                    
