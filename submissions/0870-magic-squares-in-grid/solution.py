class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def solve(ii, jj):
            nums = set()
            for i in range(ii, ii + 3):
                for j in range(jj, jj + 3):
                    if not 1 <= grid[i][j] <= 9:
                        return 0
                    if grid[i][j] in nums:
                        return 0
                    nums.add(grid[i][j])

            sums = [0] * 8
            for d in range(3):
                sums[0] += grid[ii][jj + d]
                sums[1] += grid[ii + 1][jj + d]
                sums[2] += grid[ii + 2][jj + d]
                sums[3] += grid[ii + d][jj]
                sums[4] += grid[ii + d][jj + 1]
                sums[5] += grid[ii + d][jj + 2]
                sums[6] += grid[ii + d][jj + d]
                sums[7] += grid[ii + 2 - d][jj + d]

            if not all(x == sums[0] for x in sums):
                return 0
            return 1
                    
        ret = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                ret += solve(i, j)

        return ret
                

        
        
