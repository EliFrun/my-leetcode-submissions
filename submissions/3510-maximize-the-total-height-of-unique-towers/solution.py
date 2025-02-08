class Solution:
    def maximumTotalSum(self, lis: List[int]) -> int:
        lis.sort()
        ret = 0
        highest = 1_000_000_000
        for i in range(len(lis) - 1, -1, -1):
            if lis[i] < i:
                return -1
            curr = lis[i]
            curr = min(curr, highest)
            if curr <= 0:
                return -1
            highest = curr - 1
            ret += curr

        return ret
        
