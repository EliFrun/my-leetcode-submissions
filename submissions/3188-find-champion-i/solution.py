class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        g = defaultdict(int)
        for i, l in enumerate(grid):
            for j,v in enumerate(l):
                if v == 1:
                    g[j] += 1
        
        for i in range(len(grid)):
            if g[i] == 0:
                return i
        return -1
        
