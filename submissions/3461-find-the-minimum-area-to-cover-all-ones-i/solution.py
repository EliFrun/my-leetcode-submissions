class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mx, my, mmx, mmy = float('inf'),float('inf'),-1,-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    mx = min(mx, i)
                    mmx = max(mmx, i)
                    my = min(my, j)
                    mmy = max(mmy, j)


        return max(0, (mmy - my + 1) * (mmx - mx + 1))
        
