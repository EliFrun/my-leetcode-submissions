class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        
        def traverse(i, j):
            nonlocal visited
            if (i, j) in visited:
                return 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            return grid[i][j] + traverse(i - 1, j) + traverse(i + 1, j) + traverse(i, j - 1) + traverse(i, j + 1)

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                
                ret = max(traverse(i,j), ret)

        return ret
                
