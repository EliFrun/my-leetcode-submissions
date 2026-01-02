class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2:
            c = costBoth if costBoth < cost1 + cost2 else cost1 + cost2
            return c * need2 + (need1 - need2) * min(costBoth, cost1)
        else:
            c = costBoth if costBoth < cost1 + cost2 else cost1 + cost2
            return c * need1 + (need2 - need1) * min(costBoth, cost2)




        
