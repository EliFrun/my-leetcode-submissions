class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = [0] * (len(grid) * len(grid))
        for line in grid:
            for v in line:
                m[v - 1] += 1

        ret = [0,0]
        for i in range(0, len(grid) * len(grid)):
            if m[i] == 0:
                ret[1] = i + 1

            if m[i] == 2:
                ret[0] = i + 1

        return ret
        
