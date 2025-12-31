class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        reach_start = {}
        reach_end = {}
        dirs = [0, 1, 0, -1, 0]

        for i in range(1, col + 1):
            reach_start[(0, i)] = True
            reach_end[(row + 1, i)] = True
            

        def solve(x,y, d):
            if (x, y) not in d:
                return
            if d[(x,y)]:
                return

            d[(x,y)] = True
            for i in range(4):
                dx, dy = dirs[i], dirs[i + 1]
                solve(x + dx, y + dy, d)
            
        ret = len(cells) - 1
        for x, y in reversed(cells):
            reach_start[(x,y)] = False
            reach_end[(x,y)] = False
            for i in range(4):
                dx, dy = dirs[i], dirs[i + 1]
                if (x + dx, y + dy) in reach_start and reach_start[(x + dx, y + dy)]:
                    solve(x, y, reach_start)
                if (x + dx, y + dy) in reach_end and reach_end[(x + dx, y + dy)]:
                    solve(x, y, reach_end)
            if reach_start[(x,y)] and reach_end[(x,y)]:
                return ret
            ret -= 1
        return ret
        
