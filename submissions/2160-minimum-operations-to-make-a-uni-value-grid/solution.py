class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lis = []
        for row in grid:
            lis.extend(row)

        parity = lis[0] % x
        for i in lis:
            if i % x != parity:
                return -1

        lis.sort()
        med = lis[len(lis)//2]
        return sum(abs(i - med)//x for i in lis)
        
