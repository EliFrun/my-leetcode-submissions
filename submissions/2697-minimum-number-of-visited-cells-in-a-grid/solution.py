class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        rows = [SortedList(range(len(grid[0]))) for _ in range(len(grid))]
        columns = [SortedList(range(len(grid))) for _ in range(len(grid[0]))]
        visited = set()
        q = [(1,0,0)]
        while q:
            d, x, y = heappop(q)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return d
            for i in range(rows[x].bisect_right(y + grid[x][y]) - 1, rows[x].bisect_left(y + 1) - 1, -1):
                yy = rows[x][i]
                rows[x].pop(i)
                heappush(q, (d + 1, x, yy))
            
            for i in range(columns[y].bisect_right(x + grid[x][y]) - 1, columns[y].bisect_left(x + 1) - 1, -1):
                xx = columns[y][i]
                columns[y].pop(i)
                heappush(q, (d + 1, xx, y))

        return -1
        
