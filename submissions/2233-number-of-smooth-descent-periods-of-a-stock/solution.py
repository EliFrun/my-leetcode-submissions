class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ret = 0
        cnt = 0
        prev = 1e10
        for num in prices:
            if num != prev - 1:
                ret += (cnt * (cnt + 1)) // 2
                cnt = 0
            cnt += 1
            prev = num
        
        ret += (cnt * (cnt + 1)) // 2
        
        return ret
