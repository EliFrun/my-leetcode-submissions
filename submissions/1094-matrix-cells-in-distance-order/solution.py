class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        visited = set()
        ret = []
        curr_vals = [(rCenter, cCenter)]
        next_vals = []
        while len(curr_vals) > 0:
            for i, j in curr_vals:
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                ret.append([i, j])
                for x,y in [(0,-1),(1,0), (0, 1) , (-1, 0)]:
                    if (0 <= i + x and i + x < rows) and (0 <= j + y and j + y < cols) and (i + x, j+y) not in visited:
                        next_vals.append((i + x, j + y))
                        
            curr_vals = next_vals
            next_vals = []
                
        return ret
                        
            
