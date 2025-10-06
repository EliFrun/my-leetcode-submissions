class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        curr = set([entrance])

        dirs = [0,1,0,-1,0]
        visited = set()
        ret = -1
        while curr:
            ret += 1
            nxt = set()
            for x,y in curr:
                if (x,y) != entrance and (x == 0 or y == 0):
                    return ret
                if (x,y) != entrance and (x == len(maze) - 1 or y == len(maze[0]) - 1):
                    return ret

                for i in range(4):
                    dx, dy = dirs[i], dirs[i + 1]
                    if not 0 <= x + dx < len(maze):
                        continue
                    if not 0 <= y + dy < len(maze[0]):
                        continue
                    
                    if maze[x + dx][y + dy] == '+':
                        continue
                    
                    if (x + dx, y + dy) in visited:
                        continue
                    
                    visited.add((x + dx, y + dy))
                    nxt.add((x + dx, y + dy))
            curr = nxt
        return -1
