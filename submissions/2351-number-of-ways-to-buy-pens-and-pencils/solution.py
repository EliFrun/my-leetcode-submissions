class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        big_step, small_step = max(cost1, cost2), min(cost1, cost2)
        ret = 0
        while total >= 0:
            ret += total // small_step + 1
            total -= big_step

        return ret
        
