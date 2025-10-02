class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        ret = 0
        empty = 0
        while n > 0:
            ret += n
            empty += n
            n = 0
            while empty >= e:
                n += 1
                empty -= e
                e += 1
            
        return ret
        

        
