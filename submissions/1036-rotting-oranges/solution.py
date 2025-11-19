class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.add((i,j))
        

        dirs = [0,1,0,-1,0]
        t = -1
        if not rotten:
            t += 1
        while rotten:
            t += 1
            nxt = set()
            for i,j in rotten:
                for k in range(4):
                    di, dj = dirs[k], dirs[k + 1]
                    if not 0 <= i + di < len(grid):
                        continue
                    if not 0 <= j + dj < len(grid[0]):
                        continue
                    if grid[i + di][j + dj] != 1:
                        continue
                    grid[i + di][j + dj] = 2
                    nxt.add((i + di, j + dj))
            rotten = nxt
        if all(all(x != 1 for x in grid[i]) for i in range(len(grid))):
            return t
        return -1
        
