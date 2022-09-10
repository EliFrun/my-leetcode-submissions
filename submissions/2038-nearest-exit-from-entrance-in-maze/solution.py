class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs
        visited = set()
        curr_layer = [entrance]
        next_layer = []
        
        can_leave = False
        ret = 0
        
        while len(curr_layer) > 0:
            for x,y in curr_layer:
                if (x,y) in visited:
                    continue
                visited.add((x,y))
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if can_leave:
                        if (x + dx < 0 or x + dx > len(maze) - 1 or y + dy < 0 or y + dy > (len(maze[0]) - 1)):
                            return ret
                    if ((x + dx, y + dy) not in visited and
                        (x + dx >= 0 and x + dx < len(maze) and y + dy >= 0 and y + dy < (len(maze[0]))) and
                        (maze[x + dx][y + dy] != '+')
                       ):
                        next_layer.append((x+dx, y + dy))
                
                                      
            curr_layer = next_layer
            next_layer = []
            can_leave = True
            ret += 1
                                      
        return -1
