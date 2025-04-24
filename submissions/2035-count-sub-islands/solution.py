class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        islands = []
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] != 1:
                    continue
                if (i,j) in visited:
                    continue
                v = set()
                curr = set([(i,j)])
                while curr:
                    nxt = set()
                    for x,y in curr:
                        v.add((x,y))
                        dirs = [0,1,0,-1,0]
                        for k in range(4):
                            dx, dy = dirs[k], dirs[k + 1]
                            if x + dx < 0 or y + dy < 0 or x + dx >= len(grid2) or y + dy >= len(grid2[0]):
                                continue
                            if grid2[x + dx][y + dy] != 1:
                                continue
                            nxt.add((x + dx, y + dy))
                        
                    curr = nxt - v
                visited.update(v)
                islands.append(v)

        return sum(1 for isl in islands if all(grid1[i][j] == 1 for i,j in isl))
        
