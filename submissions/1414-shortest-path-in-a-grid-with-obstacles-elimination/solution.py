class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        curr = set([(0,0)])
        visited = [[-1] * len(grid[0]) for _ in grid]
        visited[0][0] = k
        layer = -1
        while curr:
            layer += 1
            nxt = set()
            for i, j in curr:
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return layer
                dirs = [0,1,0,-1,0]
                for k in range(len(dirs) - 1):
                    di, dj = dirs[k], dirs[k + 1]
                    if i + di < 0 or i + di >= len(grid):
                        continue
                    if j + dj < 0 or j + dj >= len(grid[0]):
                        continue
                    if visited[i + di][j + dj] < visited[i][j] - grid[i + di][j + dj]:
                        visited[i + di][j + dj] = visited[i][j] - grid[i + di][j + dj]
                        nxt.add((i + di, j + dj))

            curr = nxt

        return -1
        
