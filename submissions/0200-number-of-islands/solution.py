class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()
        def bfs(i, j):
            curr = set([(i,j)])
            visited = set()
            while curr:
                nxt = set()
                steps = [(0,-1), (-1,0), (0,1), (1,0)]
                for i, j in curr:
                    visited.add((i,j))
                    for di, dj in steps:
                        if (i + di >= 0 and
                            i + di < len(grid) and
                            j + dj >= 0 and
                            j + dj < len(grid[0]) and
                            (i + di, j + dj) not in visited):
                            if grid[i+di][j + dj] == '1':
                                nxt.add((i + di, j + dj))

                curr = nxt
            return visited

        group_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                if (i,j) in explored:
                    continue
                v = bfs(i, j)
                explored.update(v)

                group_num += 1
        
        return group_num
        
