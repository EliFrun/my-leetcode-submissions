class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(row, column):
            rows = [grid[row + x][column: column + 3] for x in range(0,3)]
            nums = []
            [nums.extend(row) for row in rows]
            if sorted(nums) != list(range(1, 10)):
                return False
            columns = []
            for i in range(0,3):
                foo = []
                for j in range(0,3):
                    foo.append(grid[row + j][column + i])
                columns.append(foo)
                
            diags = [
                [grid[row][column], grid[row + 1][column + 1], grid[row + 2][column + 2]],
                [grid[row][column + 2], grid[row + 1][column + 1], grid[row + 2][column]]
            ]
            s = sum(rows[0])
            return all(sum(row) == s for row in rows) and all(sum(foo) == s for foo in columns) and all(sum(d) == s for d in diags)
        
        ret = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagic(i, j):
                    ret += 1
                    
        return ret
        
