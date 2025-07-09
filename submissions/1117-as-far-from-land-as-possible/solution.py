class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        print(*grid, sep='\n')
        curr = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    curr.add((i,j))
        
        if len(curr) == len(grid) * len(grid[0]):
            return -1

        layer = -1
        visited = set()
        while curr:
            layer += 1
            nxt = set()
            visited |= curr
            for i,j in curr:
                dirs = [0,1,0,-1,0]
                for k in range(4):
                    dx, dy = dirs[k], dirs[k + 1]
                    if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and (i + dx, j + dy) not in visited and grid[i + dx][j + dy] == 0:
                        nxt.add((i + dx, j + dy))

            curr = nxt

        return layer
