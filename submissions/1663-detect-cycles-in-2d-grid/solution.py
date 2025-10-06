class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirs = [0,1,0,-1,0]
        visited = set()
        def dfs(distance, distances, c, i, j):
            for k in range(4):
                di, dj = dirs[k], dirs[k + 1]
                if not 0 <= i + di < len(grid):
                    continue
                if not 0 <= j + dj < len(grid[0]):
                    continue
                if grid[i + di][j + dj] != c:
                    continue
                if (i + di, j + dj) in distances:
                    if distance - distances[(i + di, j + dj)] > 2:
                        return True
                    else:
                        continue
                distances[(i + di, j + dj)] = distance
                if dfs(distance + 1, distances, c, i + di, j + dj):
                    return True
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                d = {}
                if dfs(0, d, grid[i][j], i, j):
                    return True
                print(i, j, d)
                visited.update(d.keys())

        return False
        
