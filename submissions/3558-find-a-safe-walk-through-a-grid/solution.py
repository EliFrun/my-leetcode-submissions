class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]

        @cache
        def solve(h, x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            h = h if grid[x][y] == 0 else h - 1
            if h <= 0 or h <= memo[x][y]:
                return False
            else:
                memo[x][y] = h
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return True
            if h > len(grid[0]) - x + len(grid) - y:
                return True
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if solve(h, x + dx, y + dy): 
                    return True                   
            return False

        return solve(health, 0, 0)
                    
            


        
