class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        budget -= 1
        l = [(co, ca) for co,ca in zip(costs, capacity)]
        l.sort()

        stk = [(0,0)]

        ret = 0
        for i, (co, ca) in enumerate(l):
            if co > budget:
                break
            ret = max(ret, ca)
            while stk and budget - stk[-1][0] - co < 0:
                stk.pop()
            
            ret = max(ret, ca + stk[-1][1])
            
            if stk:
                stk.append((co, max(ca, stk[-1][1])))
            else:
                stk.append((co, ca))
        return ret
        
        
