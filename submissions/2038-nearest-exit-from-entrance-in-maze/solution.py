class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        curr = set()
        dirs = [0,1,0,-1,0]
        for i in range(4):
            dx = dirs[i]
            dy = dirs[i + 1]
            if entrance[0] + dx < 0 or entrance[0] + dx > len(maze) - 1:
                continue
            if entrance[1] + dy < 0 or entrance[1] + dy > len(maze[0]) - 1:
                continue
            if maze[entrance[0] + dx][entrance[1] + dy] == '+':
                continue
            curr.add((entrance[0] + dx, entrance[1] + dy))
        visited = set([tuple(entrance)])
        layer = 0
        while curr:
            layer += 1
            nxt = set()
            for x,y in curr:
                visited.add((x,y))
                dirs = [0,1,0,-1,0]
                for i in range(4):
                    dx = dirs[i]
                    dy = dirs[i + 1]
                    if x + dx < 0 or x + dx > len(maze) - 1:
                        return layer
                    if y + dy < 0 or y + dy > len(maze[0]) - 1:
                        return layer
                    if maze[x + dx][y + dy] != "+":
                        nxt.add((x + dx, y + dy))
            curr = nxt - visited

        return -1

    
        
