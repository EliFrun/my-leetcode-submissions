class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ret = []
        for i in range(len(grid) - 2):
            s = SortedList()
            for j in range(3):
                for k in range(3):
                    s.add(grid[i + k][j])
            
            line = []
            for j in range(len(grid[0]) - 2):
                line.append(s[-1])
                for k in range(3):
                    if j + 3 < len(grid[0]):
                        s.add(grid[i + k][j + 3])
                    s.remove(grid[i + k][j])
            ret.append(line)
        return ret
