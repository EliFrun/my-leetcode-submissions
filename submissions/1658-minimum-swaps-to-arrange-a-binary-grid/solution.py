class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            p = -1
            for idx, line in enumerate(grid):
                if idx < i:
                    continue
                if all(line[j] == 0 for j in range(i + 1, len(grid))):
                    p = idx
                    break
                     
            if p == -1:
                return -1
            ret += idx - i
            l = grid.pop(idx)
            grid.insert(i, l)
        
        return ret
        
