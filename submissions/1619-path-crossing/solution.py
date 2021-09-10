class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0, 0)
        visited = set()
        visited.add(curr)
        for s in path:
            if s == "N":
                curr = (curr[0] + 1, curr[1])
            if s == "E":
                curr = (curr[0], curr[1] + 1)
            if s == "S":
                curr = (curr[0] - 1, curr[1])
            if s == "W":
                curr = (curr[0], curr[1] - 1)
                
            if curr in visited:
                return True
            else:
                visited.add(curr)
                
        return False
            
