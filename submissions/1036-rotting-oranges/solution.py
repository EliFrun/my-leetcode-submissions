class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curr = set()
        good = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good.add((i,j))
                if grid[i][j] == 2:
                    curr.add((i,j))

        ret = 0
        while curr:
            nxt = set()
            for i,j in curr:
                dirs = [0,1,0,-1,0]
                for k in range(4):
                    di, dj = dirs[k], dirs[k + 1]
                    if i + di < 0 or j + dj < 0 or i + di >= len(grid) or j + dj >= len(grid[0]):
                        continue
                    if grid[i + di][j + dj] == 1:
                        good.remove((i + di, j + dj))
                        grid[i + di][j + dj] = 2
                        nxt.add((i + di, j + dj))

            ret += 1 if nxt else 0
            curr = nxt

        return ret if len(good) == 0 else -1

        
