class Solution:
    def countIslands(self, grid: List[List[int]], m: int) -> int:
        visited = [[False] * len(grid[0]) for _ in grid]
        dirs = [0,1,0,-1,0]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                q = deque([(i, j)])
                s = 0
                while q:
                    ii, jj = q.pop()
                    if visited[ii][jj]:
                        continue
                    visited[ii][jj] = True
                    s += grid[ii][jj]
                    for k in range(4):
                        di, dj = dirs[k], dirs[k + 1]
                        if not 0 <= ii + di < len(grid) or not 0 <= jj + dj < len(grid[0]):
                            continue
                        if visited[ii + di][jj + dj]:
                            continue
                        if grid[ii + di][jj + dj] == 0:
                            continue
                        q.appendleft((ii + di, jj + dj))
                if s % m == 0:
                    ret += 1

        return ret
