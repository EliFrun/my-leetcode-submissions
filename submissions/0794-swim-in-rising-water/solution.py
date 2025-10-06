class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0], 0, 0)]
        dirs = [0,1,0,-1,0]
        checked = set()
        while q:
            t, i, j = heappop(q)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return t
            for k in range(4):
                di, dj = dirs[k], dirs[k + 1]
                if not 0 <= i + di < len(grid):
                    continue
                if not 0 <= j + dj < len(grid[0]):
                    continue
                if (i + di, j + dj) in checked:
                    continue
                checked.add((i + di, j + dj))
                heappush(q, (max(t, grid[i + di][j + dj]), i + di, j + dj))
        
        return -1
            

        
