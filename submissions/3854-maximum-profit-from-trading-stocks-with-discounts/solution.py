class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n + 1)]
        for p, c in hierarchy:
            g[p - 1].append(c - 1)

        g[-1] = [0]

        @cache
        def cost_total(n):
            return present[n] + sum(cost_total(i) for i in g[n])

        
        @cache
        def solve(money, idx, parent, parent_bought):
            if idx >= len(g[parent]):
                return 0
            ret = 0
            cost = present[g[parent][idx]] // (2 if parent_bought else 1)
            upper_bound = min(money, cost_total(g[parent][idx]))
            lower_bound = 0 if idx != len(g[parent]) - 1 else min(money, upper_bound)
            for i in range(lower_bound, upper_bound + 1):
                if (v:= solve(money - i, idx + 1, parent, parent_bought) + solve(i, 0, g[parent][idx], False)) > ret:
                    ret = v
                if i >= cost:
                    if (v := future[g[parent][idx]] - cost + solve(money - i, idx + 1, parent, parent_bought) + solve(i - cost, 0, g[parent][idx], True)) > ret:
                        ret = v
            return ret

        return solve(budget, 0, -1, False)
        
        

        
