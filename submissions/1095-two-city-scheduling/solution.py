class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def solve(i, a, b):
            if i >= len(costs):
                return 0
            ret = float('inf')
            if a > 0:
                ret = min(ret, costs[i][0] + solve(i + 1, a - 1, b))
        
            if b > 0:
                ret = min(ret, costs[i][1] + solve(i + 1, a, b - 1))

            return ret

        return solve(0, len(costs)//2, len(costs)//2)
