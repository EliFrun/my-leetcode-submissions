class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = 0
        e = 0
        f = numBottles
        while f:
            ret += f
            e += f
            f = e // numExchange
            e = e % numExchange
            
        return ret
