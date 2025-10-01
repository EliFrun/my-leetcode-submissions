class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        ret = 0
        e, f = 0, nb
        while f > 0:
            ret += f
            e += f
            f = e // ne
            e = e % ne
        return ret 
        
