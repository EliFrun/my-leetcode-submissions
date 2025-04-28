class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ret = 0
        for i in range(len(cost) - 1, -1, -3):
            if i >= 1:
                ret += cost[i - 1]
            ret = ret + cost[i]

        return ret
        
