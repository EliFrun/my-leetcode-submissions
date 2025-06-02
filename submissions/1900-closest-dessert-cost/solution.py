class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        toppingCosts.sort()
        @cache
        def solve(t, i):
            if i >= len(toppingCosts):
                return t
            ret = solve(t, i + 1)
            s1 = solve(t + toppingCosts[i], i + 1)
            s2 = solve(t + 2 * toppingCosts[i], i + 1)
            return sorted([ret, s1, s2], key=lambda x: (abs(target - x), x))[0]

        return sorted([solve(x, 0) for x in baseCosts], key=lambda x: (abs(x - target), x))[0]
        
