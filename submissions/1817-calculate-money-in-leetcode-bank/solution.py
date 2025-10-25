class Solution:
    def totalMoney(self, n: int) -> int:
        ret = 0
        for i in range(n):
            ret += (i // 7 + 1) + i % 7
        return ret
            
        
